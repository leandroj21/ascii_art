from PIL import Image

class ImageASCIIArt:
    def __init__(self, path, resolution_multiplier = 3, fix_resolution = 4, thumbnail_percentage = 1) -> None:
        self.path = path
        self.width = 0
        self.height = 0
        self.pixels = None

        # The characters ordered from thinnest to boldest
        self.mapping_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

        # The amount of characters per pixel
        self.resolution_multiplier = resolution_multiplier

        # A power of 2 that makes the image clearer at printing
        self.fix_resolution = fix_resolution

        # For reducing the image size
        self.thumbnail_percentage = thumbnail_percentage

        self._load_image()
    
    def _load_image(self):
        try:
            image = Image.open(self.path)
            image.thumbnail((image.size[0] * self.thumbnail_percentage, image.size[1] * self.thumbnail_percentage))
            self.width, self.height = image.size
            self.pixels = list(image.getdata())
            self.pixels = [self.pixels[i * self.width: (i + 1) * self.width] for i in range(self.height)]
            image.close()
        except:
            raise Exception("Cannot read the image")

    def print_ascii_art(self):
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                pixel_grayscale_value = (self.pixels[i][j][0] + self.pixels[i][j][1] + self.pixels[i][j][2]) // 3
                print(self.mapping_string[(pixel_grayscale_value // self.fix_resolution) % len(self.mapping_string)] * self.resolution_multiplier, end="")
            print("\n", end="")


if __name__ == "__main__":
    image = ImageASCIIArt("path")
    image.print_ascii_art()