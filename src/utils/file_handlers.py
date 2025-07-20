import os
from pathlib import Path

class FileHandler:
    @staticmethod
    def validate_path(path):
        return os.path.exists(path) and os.access(path, os.R_OK)
    
    @staticmethod
    def create_directory(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True) 
    
    @staticmethod
    def get_file_extension(filename):
        return Path(filename).suffix.lower()
    
    @staticmethod
    def is_valid_image_file(filename):
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        return FileHandler.get_file_extension(filename) in valid_extensions