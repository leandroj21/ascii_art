
# ascii_art

Convert your favorite JPG images into ASCII art right in your console!

## Features
- Convert JPG or JPEG images to ASCII art
- Supports colored and monochrome ASCII art
## Installation
1. Clone this repository to your local machine using:
```bash
git clone https://github.com/leandroj21/ascii_art.git
```
2. Navigate to the project directory:
```bash
cd ascii_art
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run ascii_art with the following command:
```
python .\main.py path/to/your/image.jpg
```
Replace `path/to/your/image.jpg` with the actual path to the JPG/JPEG image you want to print using on the console.
### Command-line options
```
positional arguments:
  path                  The image path

options:
  -h, --help            show this help message and exit
  -c, --colored         print the image with colors (default: False)
  -i, --invert-brightness
                        invert brightness of the image pixels (default: False)
  -T THUMBNAIL_PERCENTAGE, --thumbnail-percentage THUMBNAIL_PERCENTAGE
                        adjust the image size according to that percentage, e.g. , 0.5 * height and 0.5 * width (default:
                        1.0)
  -R RESOLUTION_MULTIPLIER, --resolution-multiplier RESOLUTION_MULTIPLIER
                        number of characters printed per pixel (default: 3)
  -F {1,2,4,8,16,32,64,128}, --fix-resolution {1,2,4,8,16,32,64,128}
                        a power of 2 between 1 and 128 that makes the image clearer at printing (default: 4)
```
## Examples
With the test image:
[![Test 1](/assets/test1.jpg "Snow peak mountains wolf vector, by Mollyroselee")](https://pixabay.com/illustrations/mountains-snow-wolf-moon-nature-8149677/)
Running ``python .\main.py .\assets\test1.jpg -T 0.5`` we get:
![Test 1 result without color](/assets/test1_result_without_color.png "Result test 1 without color")
If we want to print it with color, we can use ``python .\main.py .\assets\test1.jpg -T 0.5 -c`` to get:
![Test 1 result with color](/assets/test1_result_with_color.png "Result test 1 with color")

## Credits

This project was inspired by [Robert Heaton's blogpost](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/).

**Disclaimer:** This project is for educational and recreational purposes only. It does not guarantee pixel-perfect representation of images and may vary in output quality based on the input image.
