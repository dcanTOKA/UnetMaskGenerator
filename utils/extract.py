import shutil
import zipfile


def extract_images(zip_path: str, extract_to: str):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def cleanup_extracted_files(directory: str):
    shutil.rmtree(directory)
