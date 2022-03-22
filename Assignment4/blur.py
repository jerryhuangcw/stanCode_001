"""
File: blur.py
Name: Jerry Huang
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param
    """
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            count += 1  # number of pixels being calculated
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return blurred


def main():
    """
    This program blurs the original smiley face image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
