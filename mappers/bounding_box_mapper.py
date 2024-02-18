import os
from typing import Optional, List

from models.bounding_box import BoundingBox


class BoundingBoxMapper:
    @staticmethod
    def read_file(path: str) -> str:
        with open(path, 'r') as file:
            data = file.read()
        return data

    @staticmethod
    def map_to_bounding_box(data: Optional[str] = None, path: Optional[str] = None) -> List[BoundingBox]:
        if path is not None:
            if os.path.exists(path):
                data = BoundingBoxMapper.read_file(path)
            else:
                raise FileNotFoundError(f"The file at {path} was not found.")

        if data is None:
            raise ValueError("No data provided.")

        bounding_box_data: List[BoundingBox] = []

        lines = data.strip().split('\n')
        for line in lines:
            parts = line.split()
            class_id = int(parts[0])
            boundary_box = [float(part) for part in parts[1:]]
            bounding_box = BoundingBox(class_id=class_id, boundary_box=boundary_box)
            bounding_box_data.append(bounding_box)
        return bounding_box_data
