"""
File: mirror_lake.py
Name: Jerry Huang
----------------------------------
This file reads in mt-rainier.jpg and makes a new image
that creates a mirror lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original color image
    :return: vertically mirrored image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)  # original
            new_img_pixel1 = new_img.get_pixel(x, y)  # upper
            new_img_pixel2 = new_img.get_pixel(x, new_img.height-1-y)  # bottom(vertical mirror)
            new_img_pixel1.red = img_pixel.red
            new_img_pixel1.green = img_pixel.green
            new_img_pixel1.blue = img_pixel.blue
            new_img_pixel2.red = img_pixel.red
            new_img_pixel2.green = img_pixel.green
            new_img_pixel2.blue = img_pixel.blue
    return new_img


def main():
    """
    This program shows the original image and creates vertically mirrored image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
