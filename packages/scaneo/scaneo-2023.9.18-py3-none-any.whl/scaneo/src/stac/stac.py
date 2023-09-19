from pystac import Catalog, MediaType, Collection
import os
import json
from src.storage import Storage
import shutil


geotiff_type = "image/tiff; application=geotiff"
allowed_media_types = [media_type.value for media_type in MediaType]
label_extension = "https://stac-extensions.github.io/label/v1.0.1/schema.json"
scaneo_asset = "labels"
scaneo_labels_and_colors = "labels:colors"
image_mode = os.getenv("IMAGE")
asset_name = image_mode + "_labels.geojson"


def is_stac(storage):
    return storage.exists("catalog.json")


def get_stac_catalog() -> Catalog:
    storage = Storage()
    catalog_file = [f for f in storage.list() if f.endswith("catalog.json")]
    if not catalog_file:
        return None
    catalog_path = storage.get_url(catalog_file[0])
    catalog = Catalog.from_file(catalog_path)
    return catalog


def save_json(file_path, json_file):
    with open(file_path, "w") as f:
        json.dump(json_file, f)


class Stac:
    def __init__(self, catalog=get_stac_catalog()):
        self.catalog = catalog

    def get_catalog(self):
        return self.catalog

    def collections(self):
        return list(self.catalog.get_children())

    def collection_links(self):
        return self.catalog.get_child_links()

    def get_items_paths(self, collection):
        collection_path = collection.get_self_href()
        with open(collection_path, "r") as collection_item:
            collection_json = json.load(collection_item)
        relative_hrefs = [
            link["href"] for link in collection_json["links"] if link["rel"] == "item"
        ]
        folder_path = os.path.dirname(collection_path)
        paths = [
            os.path.normpath(os.path.join(folder_path, relative_href))
            for relative_href in relative_hrefs
        ]
        return paths

    def find_label_collection(self):
        return next(
            filter(
                lambda collection: label_extension in collection.stac_extensions,
                self.collections(),
            )
        )

    def create_label_collection(self):
        catalog_path = self.catalog.self_href
        catalog_dir = catalog_path.replace("catalog.json", "")
        labels_dir = os.path.join(catalog_dir, "labels")
        print("WARNING: no label collection found, creating one in", labels_dir)
        if not os.path.exists(labels_dir):
            os.makedirs(labels_dir)
        source_collection_path = self.source_collection().self_href
        shutil.copy(source_collection_path, labels_dir)
        label_collection_path = labels_dir + "/collection.json"
        with open(label_collection_path, "r") as collection_item:
            collection_json = json.load(collection_item)
            collection_json["id"] = "labels"
            collection_json["description"] = "Labels"
            collection_json["links"] = []
            collection_json["stac_extensions"] = [label_extension]
            collection_json["summaries"] = {
                scaneo_labels_and_colors: [],
                "label:classes": [{"classes": [], "name": "label"}],
                "label:type": image_mode,
            }
            save_json(label_collection_path, collection_json)
            collection = Collection.from_dict(collection_json)
            self.catalog.add_child(collection)
            self.catalog.save()
        return collection

    def label_collection(self):
        try:
            return self.find_label_collection()
        except StopIteration:
            return self.create_label_collection()

    def get_labels(self):
        label_collection = self.label_collection()
        label_classes = label_collection.summaries.to_dict()["label:classes"]
        if len(label_classes) > 1:
            print("WARNING: more than one label class found, using the first one")
        target_labels = label_classes[0]
        return target_labels["classes"]

    def get_label_colors(self):
        label_collection = self.label_collection()
        summaries = label_collection.summaries.to_dict()
        return summaries["scaeno:colors"] if "scaeno:colors" in summaries else []

    def get_labels_and_colors(self):
        labels = self.get_labels()
        colors = self.get_label_colors()
        labels_and_colors = [{"name": label} for label in labels]
        for i, label in enumerate(labels_and_colors):
            if label["name"] in colors:
                labels_and_colors[i]["color"] = colors[label["name"]]
        return labels_and_colors

    def find_label_item(self, image_path):
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        label_paths = self.get_items_paths(self.label_collection())
        if not label_paths:
            return None
        for path in label_paths:
            item_name = os.path.splitext(os.path.basename(path))[0]
            if item_name == image_name:
                return path
        return None

    def create_label_item(self, image_path):
        name = os.path.splitext(os.path.basename(image_path))[0]
        collection_path = self.label_collection().get_self_href()
        label_dir = collection_path.replace("collection.json", name)
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        source_item = self.find_source_item(image_path)
        shutil.copy(source_item, label_dir)
        label_path = label_dir + f"/{name}.json"
        with open(label_path, "r") as label_item:
            label = json.load(label_item)
            label["stac_extensions"].append(label_extension)
            label["collection"] = "labels"
            label["assets"] = {}
            label["properties"]["label:properties"] = ["label"]
            label["properties"]["label:description"] = "Item label"
            label["properties"]["label:type"] = "vector"
            links = []
            links.append(
                {
                    "rel": "root",
                    "href": os.path.relpath(self.catalog.self_href, label_dir),
                    "type": "application/json",
                }
            )
            links.append(
                {
                    "rel": "collection",
                    "href": os.path.relpath(collection_path, label_dir),
                    "type": "application/json",
                }
            )
            links.append(
                {
                    "rel": "source",
                    "href": os.path.relpath(source_item, label_dir),
                    "type": "application/json",
                }
            )
            label["links"] = links
            save_json(label_path, label)

        ## Add item link to collection
        with open(collection_path, "r") as collection_item:
            collection_json = json.load(collection_item)
            collection_json["links"].append(
                {
                    "rel": "item",
                    "href": "./" + name + "/" + name + ".json",
                    "type": "application/json",
                }
            )
            save_json(collection_path, collection_json)
        return label_dir + f"/{name}.json"

    def save_labels(self, labels):
        label_collection = self.label_collection().get_self_href()
        with open(label_collection, "r") as item:
            json_item = json.load(item)
            label_names = [label["name"] for label in labels]
            labels_and_colors = [{label["name"]: label["color"]} for label in labels]
            labels_and_colors_dictionary = {}
            for pair in labels_and_colors:
                for key, value in pair.items():
                    labels_and_colors_dictionary[key] = value
            json_item["summaries"]["label:classes"][0]["classes"] = label_names
            json_item["summaries"]["scaeno:colors"] = labels_and_colors_dictionary
            save_json(label_collection, json_item)

    def get_annotations(self, image_path):
        label_item = self.find_label_item(image_path)
        if not label_item:
            label_item = self.create_label_item(image_path)
        item_json = json.load(open(label_item))
        label_item_dir = os.path.dirname(label_item)
        assets = item_json["assets"]
        if scaneo_asset in assets:
            return json.load(open(label_item_dir + "/" + asset_name))
        else:
            geojson = {
                "type": "FeatureCollection",
                "features": [item_json],
            }
            return geojson

    def find_source_item(self, image_path):
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        source_paths = self.get_items_paths(self.source_collection())
        for path in source_paths:
            item_name = os.path.splitext(os.path.basename(path))[0]
            if item_name == image_name:
                return path

    def source_collection(self):
        collections = self.collections()
        return next(
            filter(
                lambda collection: not label_extension in collection.stac_extensions,
                collections,
            )
        )

    def add_bboxes(self, source_items_paths):
        names_and_bboxes = []
        for image_item_path in source_items_paths:
            with open(image_item_path, "r") as item:
                json_item = json.load(item)
                image_name = json_item["id"]
                image_info = json_item["assets"][image_name]
                image_bbox = json_item["bbox"]
                image_relative_path = image_info["href"]
                image_path = os.path.normpath(
                    os.path.join(os.path.dirname(image_item_path), image_relative_path)
                )
                dict = {"name": image_path, "bbox": image_bbox}
                names_and_bboxes.append(dict)
        return names_and_bboxes

    def get_image_paths(self, source_items_paths):
        image_paths = []
        for image_item_path in source_items_paths:
            with open(image_item_path, "r") as item:
                json_item = json.load(item)
                image_name = json_item["id"]
                image_info = json_item["assets"][image_name]
                image_relative_path = image_info["href"]
                image_path = os.path.normpath(
                    os.path.join(os.path.dirname(image_item_path), image_relative_path)
                )
                image_paths.append(image_path)
        return image_paths

    def get_image_bboxes(self, source_items_paths):
        image_bboxes = []
        for image_item_path in source_items_paths:
            with open(image_item_path, "r") as item:
                json_item = json.load(item)
                image_bbox = json_item["bbox"]
                image_bboxes.append(image_bbox)
        return image_bboxes

    def save_classification(self, image_path, feature):
        label_item = self.find_label_item(image_path)
        if not label_item:
            label_item = self.create_label_item(image_path)
        with open(label_item, "r") as item:
            json_item = json.load(item)
            json_item["properties"]["label"] = feature.properties["label"]
            asset = {
                scaneo_asset: {
                    "href": "./" + asset_name,
                    "title": "Label",
                    "type": "application/geo+json",
                }
            }
            json_item["assets"] = asset
            save_json(label_item, json_item)

    def add_scaneo_asset(self, image_path):
        label_item = self.find_label_item(image_path)
        if label_item is None:
            label_item = self.create_label_item(image_path)
        with open(label_item, "r") as item:
            json_item = json.load(item)
            if scaneo_asset not in json_item["assets"]:
                asset = {
                    scaneo_asset: {
                        "href": "./" + asset_name,
                        "title": "Label",
                        "type": "application/geo+json",
                    }
                }
                json_item["assets"].append(asset)
            save_json(label_item, json_item)

    def save(self, name, geojson_string):
        geojson = json.loads(geojson_string.json())
        image_path = name
        self.add_scaneo_asset(image_path)
        label_item = self.find_label_item(image_path)
        label_item_dir = os.path.dirname(label_item)
        print()
        storage = Storage()
        storage.save(
            label_item_dir + "/" + asset_name,
            json.dumps(geojson),
        )
