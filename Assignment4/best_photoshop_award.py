"""
File: best_photoshop_award.py
Name: Jerry Huang
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""


from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.4

# Controls the upper bound for black pixel
BLACK_PIXEL = 110


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 me: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:  # green screen
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background.
    Design Concept: Need to line up for 3 hours to get into Don Don Donki, what the hell.
    """
    fg = SimpleImage('image_contest/figure008.jpeg')
    bg = SimpleImage('image_contest/donki.jpg')
    fg.make_as_big_as(bg)
    combined_img = combine(bg, fg)
    combined_img.show()


if __name__ == '__main__':
    main()
