import os
import argparse
from image_filter import BrightnessFilter, ContrastFilter, BlurFilter, SaturationFilter
from image_processor import ImageProcessor
from helper import parse_filters

def main():
    parser = argparse.ArgumentParser(description="Process images with multiple filters.")
    parser.add_argument('--dir', required=True, help="Source directory of images")
    parser.add_argument('--filters', required=True, help="Filters to apply with values, e.g., 'blur=5.0,brightness=2.4'")
    args = parser.parse_args()

    source_directory = args.dir
    filter_params = parse_filters(args.filters)

    filter_classes = {
        'brightness': BrightnessFilter,
        'contrast': ContrastFilter,
        'blur': BlurFilter,
        'saturation': SaturationFilter
    }

    for filter_type, values in filter_params.items():
        if filter_type in filter_classes:
            for filter_value in values:
                image_filter = filter_classes[filter_type](filter_value)

                base_name = os.path.basename(source_directory.rstrip('/'))
                parent_directory = os.path.dirname(source_directory.rstrip('/'))
                destination_directory = os.path.join(parent_directory, f"{base_name}_{filter_type}_{filter_value}")

                processor = ImageProcessor(image_filter, filter_type, filter_value)
                processor.process_directory(source_directory, destination_directory)
        else:
            print(f"Filter '{filter_type}' is not recognized.")

if __name__ == "__main__":
    main()
