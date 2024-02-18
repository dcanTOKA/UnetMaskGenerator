import os
import zipfile
from typing import Union

from PIL import Image

from mappers.bounding_box_mapper import BoundingBoxMapper
from models.image_annotation import ImageAnnotation
from utils.extract import extract_images, cleanup_extracted_files


class AnnotationLoader:
    def __init__(self, zip_path: str, images_zip_path: str):
        self.zip_path = zip_path
        self.images_zip_path = images_zip_path
        self.annotations = []

    def load_annotations(self):
        extract_images(self.images_zip_path, "temp_images")
        annotations = []
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall("temp_annotations")
            for filename in os.listdir("temp_annotations"):
                if filename.endswith(".txt"):
                    image_annotation = self.process_annotation_file(
                        os.path.join("temp_annotations", filename),
                        filename, "temp_images")
                    if image_annotation:
                        annotations.append(image_annotation)
            cleanup_extracted_files("temp_annotations")
        cleanup_extracted_files("temp_images")
        self.annotations = annotations

    def process_annotation_file(self, file_path: str, file_name: str, images_directory: str) -> ImageAnnotation:
        with open(file_path, 'r') as file:
            data = file.read().strip()
            boundary_boxes = BoundingBoxMapper.map_to_bounding_box(data=data)

            base_name = file_name.split('.')[0]
            image_path = self.find_image_file(base_name, images_directory)

            if image_path:
                image = Image.open(image_path)
                width, height = image.size
                image_annotation = ImageAnnotation(
                    image_name=base_name,
                    extension=image_path.split('.')[-1],
                    boundary_boxes=boundary_boxes,
                    width=width,
                    height=height
                )
                return image_annotation

    def find_image_file(self, base_name: str, directory: str) -> Union[str, None]:
        last_dir = self.images_zip_path.split('/')[-1]
        directory = f"{directory}/{last_dir.split('.')[0]}"
        for filename in os.listdir(directory):
            if filename.startswith(base_name):
                return os.path.join(directory, filename)
        return None
