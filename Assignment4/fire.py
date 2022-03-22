"""
File: fire.py
Name: Jerry Huang
---------------------------------
This file contains a method called highlight_fires which detects the
pixels that are recognized as fire and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original color image.
    :return: Highlighted forest fire image.
    """
    fire_img = SimpleImage(filename)
    for pixel in fire_img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg*HURDLE_FACTOR:  # find forest fire
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:  # gray scale non-fire locations
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fire_img


def main():
    """
    This program highlights the forest fire in the image for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
