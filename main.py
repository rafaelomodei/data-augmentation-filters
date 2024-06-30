import os
import argparse
from image_filter import BrightnessFilter, ContrastFilter, BlurFilter, SaturationFilter
from image_processor import ImageProcessor

def main():
    parser = argparse.ArgumentParser(description="Process images with a filter.")
    parser.add_argument('--dir', required=True, help="Source directory of images")
    parser.add_argument('--filter', choices=['brightness', 'contrast', 'blur', 'saturation'], required=True, help="Type of filter to apply")
    parser.add_argument('--value', type=float, default=1.5, help="Value of the filter to apply")
    args = parser.parse_args()

    source_directory = args.dir
    filter_type = args.filter
    filter_value = args.value

    base_name = os.path.basename(source_directory.rstrip('/'))
    parent_directory = os.path.dirname(source_directory.rstrip('/'))
    destination_directory = os.path.join(parent_directory, f"{base_name}_{filter_type}_{filter_value}")

    filter_classes = {
        'brightness': BrightnessFilter,
        'contrast': ContrastFilter,
        'blur': BlurFilter,
        'saturation': SaturationFilter
    }

    image_filter = filter_classes[filter_type](filter_value)

    processor = ImageProcessor(image_filter)
    processor.process_directory(source_directory, destination_directory)

if __name__ == "__main__":
    main()
