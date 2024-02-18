from typing import List
from pydantic import BaseModel


class BoundingBox(BaseModel):
    class_id: int
    boundary_box: List[float]
