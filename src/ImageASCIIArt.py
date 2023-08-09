from PIL import Image


class ImageASCIIArt:
    """
    A class used to represent an Image that will be printed as ASCII art

    ...

    Attributes
    ----------
    path : str
        The path of the image
    thumbnail_percentage : float
        Used for reducing the image size in a percentage (default is 1.0)
    width : int
        The width of the image
    height : int
        The height of the image
    pixels : list
        A 2D list of the pixels
    mapping_string : str
        The string that represents the different grayscale values

    Methods
    -------
    _load_image()
        Loads the image into the class ImageASCIIArt
    print_ascii_art(resolution_multiplier = 3, fix_resolution = 4)
        Print the image using ASCII characters
    """

    def __init__(self, path, thumbnail_percentage = 1.0) -> None:
        """
        Parameters
        ----------
        path : str
            The path of the image
        thumbnail_percentage : float, optional
            Used for reducing the image size in a percentage (default is 1.0)
        """
        self.path = path
        self.thumbnail_percentage = thumbnail_percentage
        self.width = 0
        self.height = 0
        self.pixels = None

        # The characters ordered from thinnest to boldest
        self.mapping_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

        self._load_image()

    def _load_image(self):
        """Loads the image into the class ImageASCIIArt"""

        try:
            image = Image.open(self.path)
            image.thumbnail((image.size[0] * self.thumbnail_percentage, image.size[1] * self.thumbnail_percentage))
            self.width, self.height = image.size
            self.pixels = list(image.getdata())
            self.pixels = [self.pixels[i * self.width: (i + 1) * self.width] for i in range(self.height)]
            image.close()
        except:
            raise Exception("Cannot read the image")

    def print_ascii_art(self, resolution_multiplier = 3, fix_resolution = 4):
        """Print the image using ASCII characters

        Parameters
        ----------
        resolution_multiplier : int, optional
            The amount of characters per pixel (default is 3)
        fix_resolution : int, optional
            A power of 2 in [1, 128] that makes the image clearer at printing (default is 4)
        """

        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                pixel_grayscale_value = (self.pixels[i][j][0] + self.pixels[i][j][1] + self.pixels[i][j][2]) // 3
                print(self.mapping_string[(pixel_grayscale_value // fix_resolution) % len(self.mapping_string)] * resolution_multiplier, end="")
            print("\n", end="")
