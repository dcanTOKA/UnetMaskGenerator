# This is a sample Python script.
import argparse

from services.annotation_loader_service import AnnotationLoader
from services.mask_generator_service import MaskGenerator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate masks from annotations.")
    parser.add_argument("--zip_path", type=str, default="./data/labels_bone-parts-in-hand.zip", help="Path to the zip file containing labels.")
    parser.add_argument("--images_zip_path", type=str, default="./data/all.zip", help="Path to the zip file containing images.")
    parser.add_argument("--output_dir", type=str, default="./masks/", help="Directory to save generated masks.")

    args = parser.parse_args()

    annotation_loader = AnnotationLoader(zip_path=args.zip_path, images_zip_path=args.images_zip_path)
    annotation_loader.load_annotations()

    mask_generator = MaskGenerator(output_dir=args.output_dir)
    mask_generator.generate_mask(annotation_loader.annotations)
