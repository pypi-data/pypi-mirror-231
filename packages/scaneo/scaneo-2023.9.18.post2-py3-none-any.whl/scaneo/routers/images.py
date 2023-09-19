from fastapi import APIRouter, HTTPException
from starlette.responses import StreamingResponse
from src.image import get_image_data, get_tile_data, ready_image, get_bbox
from src.image.errors import ImageOutOfBounds
from src.storage import Storage
from src.stac import is_stac, Stac


router = APIRouter(prefix="/images", tags=["images"])


@router.get("")
def get_images():
    try:
        storage = Storage()
        if is_stac(storage):
            stac = Stac()
            source_items = stac.get_items_paths(stac.source_collection())
            image_paths = stac.get_image_paths(source_items)
            image_bboxes = stac.get_image_bboxes(source_items)
            path_and_bboxes = [
                {"name": image_path, "bbox": image_bbox}
                for image_path, image_bbox in zip(image_paths, image_bboxes)
            ]
            return (
                path_and_bboxes
                if path_and_bboxes
                else HTTPException(status_code=404, detail="Images not found")
            )
        images = [
            f for f in storage.list() if f.endswith(".tif")
        ]  # deberia ser .tiff también
        paths = [storage.get_url(image) for image in images]
        bboxes = [get_bbox(image) for image in paths]
        return [{"name": image, "bbox": bbox} for image, bbox in zip(images, bboxes)]
    except Exception as e:
        print("error images:get_images", e)
        return HTTPException(status_code=500, detail=str(e))


@router.get("/{image:path}/{z}/{x}/{y}.png")
def retrieve_image_tile(
    image: str,
    z: int,
    x: int,
    y: int,
    bands: str = "4,3,2",
    stretch: str = "0,3000",
    palette: str = "viridis",
):
    storage = Storage()
    image_url = storage.get_url(image)
    tile_size = (256, 256)
    if len(bands) == 1:
        bands = int(bands)
    else:
        bands = tuple([int(band) for band in bands.split(",")])
    stretch = tuple([float(v) for v in stretch.split(",")])
    try:
        tile = get_tile_data(image_url, (x, y, z), bands, tile_size)
        tile = get_image_data(tile, stretch, palette)
        image = ready_image(tile)
        return StreamingResponse(image, media_type="image/png")
    except ImageOutOfBounds as error:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
        return None
    except Exception as e:
        # raise HTTPException(status_code=500, detail="Could not retrieve tile")
        return None
