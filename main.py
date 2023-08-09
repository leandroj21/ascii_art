import argparse
from src.ImageASCIIArt import ImageASCIIArt

def restricted_float(x: any) -> float:
    try:
        x = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError("%r not a floating-point literal" % (x,))

    if x <= 0.0 or x >= 1.0:
        raise argparse.ArgumentTypeError("%r not in range (0.0, 1.0]"%(x,))
    return x

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ascii_art",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("path", help="The image path")
    parser.add_argument("-c", "--colored", action="store_true", default=False, help="print the image with colors")
    parser.add_argument("-i", "--invert-brightness", action="store_true", default=False, help="invert brightness of the image pixels")
    parser.add_argument("-T", "--thumbnail-percentage", type=restricted_float, default=1.0, help="adjust the image size according to that percentage, e.g. , 0.5 * height and 0.5 * width")
    parser.add_argument("-R", "--resolution-multiplier", type=int, default=3, help="number of characters printed per pixel")
    parser.add_argument("-F", "--fix-resolution", type=int, default=4, choices=[2 ** i for i in range(8)], help="a power of 2 between 1 and 128 that makes the image clearer at printing")

    args = vars(parser.parse_args())

    image = ImageASCIIArt(args["path"], thumbnail_percentage=args["thumbnail_percentage"])
    image.print_ascii_art(invert_brightness=args["invert_brightness"], colored=args["colored"], resolution_multiplier=args["resolution_multiplier"], fix_resolution=args["fix_resolution"])
