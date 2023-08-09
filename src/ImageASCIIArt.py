from PIL import Image
from colorama import Fore, Style

# [COLOR, INITIAL RGB RANGE, FINAL RGB RANGE]
_colors_comparisons = [
    [Fore.BLACK, (0, 0, 0), (85, 85, 85)],
    [Fore.RED, (85, 0, 0), (170, 85, 85)],
    [Fore.GREEN, (0, 85, 0), (85, 170, 85)],
    [Fore.YELLOW, (85, 85, 0), (170, 170, 85)],
    [Fore.BLUE, (0, 0, 85), (85, 85, 170)],
    [Fore.MAGENTA, (85, 0, 85), (170, 85, 170)],
    [Fore.CYAN, (0, 85, 85), (85, 170, 170)],
    [Fore.WHITE, (85, 85, 85), (170, 170, 170)],
    [Fore.LIGHTBLACK_EX, (170, 170, 170), (191, 191, 191)],
    [Fore.LIGHTRED_EX, (170, 0, 0), (255, 85, 85)],
    [Fore.LIGHTGREEN_EX, (0, 170, 0), (85, 255, 85)],
    [Fore.LIGHTYELLOW_EX, (170, 170, 0), (255, 255, 85)],
    [Fore.LIGHTBLUE_EX, (0, 0, 170), (85, 85, 255)],
    [Fore.LIGHTMAGENTA_EX, (170, 0, 170), (255, 85, 255)],
    [Fore.LIGHTCYAN_EX, (0, 170, 170), (85, 255, 255)],
    [Fore.LIGHTWHITE_EX, (170, 170, 170), (255, 255, 255)]
]

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
    print_ascii_art(resolution_multiplier=3, fix_resolution=4, invert_brightness=False)
        Print the image using ASCII characters
    """

    def __init__(self, path, thumbnail_percentage=1.0) -> None:
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

    def _load_image(self) -> None:
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

    def _is_rgb_within_range(self, rgb:tuple, lower_bound:tuple, upper_bound:tuple) -> bool:
        """Select the color that could represent a pixel

        Parameters
        ----------
        rgb : tuple
            RGB tuple that we need to know if it is between lower_bound and upper_bound
        lower_bound : tuple
            RGB tuple that is the lower bound in the comparison
        upper_bound : tuple
            RGB tuple that is the upper bound in the comparison
        """
        r, g, b = rgb
        lower_r, lower_g, lower_b = lower_bound
        upper_r, upper_g, upper_b = upper_bound
        
        within_r = lower_r <= r <= upper_r
        within_g = lower_g <= g <= upper_g
        within_b = lower_b <= b <= upper_b
        
        return within_r and within_g and within_b

    def _select_printing_color(self, pixel:tuple) -> str:
        """Select the color that could represent a pixel

        Parameters
        ----------
        pixel : tuple
            Pixel in RGB that will be represented with a color from colorama color pallete
        """
        for color_comparison in _colors_comparisons:
            if self._is_rgb_within_range(pixel, color_comparison[1], color_comparison[2]):
                return color_comparison[0]
        return Fore.WHITE

    def print_ascii_art(self, resolution_multiplier=3, fix_resolution=4, invert_brightness=False, colored=False) -> None:
        """Print the image using ASCII characters

        Parameters
        ----------
        resolution_multiplier : int, optional
            The amount of characters per pixel (default is 3)
        fix_resolution : int, optional
            A power of 2 in [1, 128] that makes the image clearer at printing (default is 4)
        invert_brightness : bool, optional
            Invert the brightnesses of the pixels (default is False)
        """

        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                pixel_grayscale_value = (self.pixels[i][j][0] + self.pixels[i][j][1] + self.pixels[i][j][2]) // 3

                if invert_brightness:
                    index_mapping = ((abs(pixel_grayscale_value - 255)) // fix_resolution) % len(self.mapping_string)
                else:
                    index_mapping = (pixel_grayscale_value // fix_resolution) % len(self.mapping_string)
                
                if colored:
                    print(f"{self._select_printing_color(self.pixels[i][j])}{self.mapping_string[index_mapping] * resolution_multiplier}{Style.RESET_ALL}", end="")
                else:
                    print(self.mapping_string[index_mapping] * resolution_multiplier, end="")
            print("\n", end="")
