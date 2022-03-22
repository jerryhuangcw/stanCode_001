"""
File: green_screen.py
Name: Jerry Huang
-------------------------------
This file creates a new image that uses MillenniumFalcon.png
as background and replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: millennium falcon image
    :param figure_img: green screen figure
    :return: the green screen pixels are replaced by pixels of background image
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            pixel_fg = figure_img.get_pixel(x, y)
            bigger = max(pixel_fg.red, pixel_fg.blue)
            if pixel_fg.green > bigger*2:  # green screen
                pixel_bg = background_img.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return figure_img


def main():
    """
    This program replaces the green pixels in the figure image(green screen)
    with the background pixels to create a new scene.
    """
    background = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(background, figure)
    result.show()


if __name__ == '__main__':
    main()
