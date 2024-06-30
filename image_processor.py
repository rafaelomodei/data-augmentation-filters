import os
from PIL import Image
import shutil

class ImageProcessor:
    def __init__(self, image_filter, filter_name, filter_value):
        self.image_filter = image_filter
        self.filter_name = filter_name
        self.filter_value = filter_value

    def process_directory(self, source_directory, destination_directory):
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        print(f"Processing filter: {self.filter_name} with value: {self.filter_value}")

        files = os.listdir(source_directory)
        total_files = len(files)

        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(source_directory, filename)

            if os.path.isfile(file_path):
                base_name, ext = os.path.splitext(filename)

                if ext.lower() in ['.jpg', '.jpeg', '.png']:
                    with Image.open(file_path) as image:
                        processed_image = self.image_filter.apply(image)
                        new_filename = f"{base_name}_{self.filter_name}_{self.filter_value}{ext}"
                        destination_path = os.path.join(destination_directory, new_filename)
                        processed_image.save(destination_path)

                    self._copy_text_file(base_name, source_directory, destination_directory, new_filename)

                self._show_progress(index, total_files)

        print(f"\nImages processed and saved in: {destination_directory}")

    def _copy_text_file(self, base_name, source_directory, destination_directory, new_image_filename):
        txt_filename = f"{base_name}.txt"
        source_txt_path = os.path.join(source_directory, txt_filename)
        
        if os.path.isfile(source_txt_path):
            new_txt_filename = os.path.splitext(new_image_filename)[0] + '.txt'
            destination_txt_path = os.path.join(destination_directory, new_txt_filename)
            shutil.copy(source_txt_path, destination_txt_path)

    def _show_progress(self, current, total):
        progress = (current / total) * 100
        print(f"Progress: {progress:.2f}% ({current}/{total})", end='\r')
