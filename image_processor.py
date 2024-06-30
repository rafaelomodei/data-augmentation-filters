import os
from PIL import Image

class ImageProcessor:
    def __init__(self, image_filter):
        self.image_filter = image_filter

    def process_directory(self, source_directory, destination_directory):
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        files = os.listdir(source_directory)
        total_files = len(files)

        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(source_directory, filename)

            if os.path.isfile(file_path):
                with Image.open(file_path) as image:
                    processed_image = self.image_filter.apply(image)
                    destination_path = os.path.join(destination_directory, filename)
                    processed_image.save(destination_path)

                self._show_progress(index, total_files)

        print(f"\nImages processed and saved in: {destination_directory}")

    def _show_progress(self, current, total):
        progress = (current / total) * 100
        print(f"Progress: {progress:.2f}% ({current}/{total})", end='\r')
