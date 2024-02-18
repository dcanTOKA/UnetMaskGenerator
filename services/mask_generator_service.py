import os
from typing import List

from PIL import Image, ImageDraw

from models.image_annotation import ImageAnnotation


class MaskGenerator:
    def __init__(self, output_dir: str = './masks/'):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_mask(self, image_annotations: List[ImageAnnotation]):

        for image_annotation in image_annotations:

            mask = Image.new('L', (image_annotation.width, image_annotation.height), 0)
            draw = ImageDraw.Draw(mask)

            for boundary_box_obj in image_annotation.boundary_boxes:
                x_center, y_center, width, height = boundary_box_obj.boundary_box
                x_min = int((x_center - width / 2) * image_annotation.width)
                y_min = int((y_center - height / 2) * image_annotation.height)
                x_max = int((x_center + width / 2) * image_annotation.width)
                y_max = int((y_center + height / 2) * image_annotation.height)

                if boundary_box_obj.class_id == 1:
                    fill_value = 255
                else:
                    fill_value = 128

                draw.rectangle((x_min, y_min, x_max, y_max), fill=fill_value)

            mask_path = f"{self.output_dir}{image_annotation.image_name}.png"
            mask.save(mask_path)
            print(f"Combined mask saved to {mask_path}")
