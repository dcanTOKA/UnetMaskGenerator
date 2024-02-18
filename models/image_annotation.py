from typing import List

from pydantic import BaseModel

from models.bounding_box import BoundingBox


class ImageAnnotation(BaseModel):
    image_name: str
    extension: str
    boundary_boxes: List[BoundingBox]
    width: int
    height: int
