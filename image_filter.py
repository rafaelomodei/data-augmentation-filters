from PIL import ImageEnhance, ImageFilter as PILImageFilter
from abc import ABC, abstractmethod

class ImageFilter(ABC):
    @abstractmethod
    def apply(self, image):
        pass

class BrightnessFilter(ImageFilter):
    def __init__(self, brightness_factor=1.5):
        self.brightness_factor = brightness_factor

    def apply(self, image):
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(self.brightness_factor)

class ContrastFilter(ImageFilter):
    def __init__(self, contrast_factor=1.5):
        self.contrast_factor = contrast_factor

    def apply(self, image):
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(self.contrast_factor)

class BlurFilter(ImageFilter):
    def __init__(self, blur_radius=2):
        self.blur_radius = blur_radius

    def apply(self, image):
        return image.filter(PILImageFilter.GaussianBlur(self.blur_radius))

class SaturationFilter(ImageFilter):
    def __init__(self, saturation_factor=1.5):
        self.saturation_factor = saturation_factor

    def apply(self, image):
        enhancer = ImageEnhance.Color(image)
        return enhancer.enhance(self.saturation_factor)
