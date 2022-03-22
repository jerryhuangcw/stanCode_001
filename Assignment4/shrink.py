"""
File: shrink.py
Name: Jerry Huang
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original color image
    :return img: SimpleImage, shrink image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            img_pixel = img.get_pixel(x*2, y*2)  # get original pixel, x = 0,2,4,6,....
            new_img_pixel = new_img.get_pixel(x, y)  # shrink image, x = 0,1,2,3,....
            new_img_pixel.red = img_pixel.red
            new_img_pixel.green = img_pixel.green
            new_img_pixel.blue = img_pixel.blue
    return new_img


def main():
    """
    This program shrinks 50% of the original image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
