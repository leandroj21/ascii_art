from PIL import Image

class ImageASCIIArt:
    def __init__(self, path) -> None:
        self.path = path
        self.width = 0
        self.height = 0
        self.pixels = None

        self._load_image()
    
    def _load_image(self):
        try:
            image = Image.open(self.path)
            self.pixels = list(image.getdata())
            self.width, self.height = image.size
            self.pixels = [self.pixels[i * self.width: (i + 1) * self.width] for i in range(self.height)]
            image.close()
        except:
            raise Exception("Cannot read the image")
    
    def print_ascii_art(self):
        pass

if __name__ == "__main__":
    image = ImageASCIIArt("path")
    print(image.pixels[0])