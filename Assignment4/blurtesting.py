"""
File: blur.py
Name: Jerry Huang
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    img=SimpleImage('images/smiley-face.png')
    new_img = SimpleImage.blank(img.width,img.height)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y)
            new_img_pixel = new_img.get_pixel(x,y)
            new_img_pixel.green = img_pixel.green
            new_img_pixel.blue = img_pixel.blue
            new_img_pixel.red = img_pixel.red
            for new_img_pixel in new_img:
                new_img_pixel = new_img_pixel.red+new_img_pixel.green+new_img_pixel.blue
                new_img_pixel1 = (0, 0, 0)
                new_img_pixel2 = (0, 0, 0)
                new_img_pixel3 = (0, 0, 0)
                new_img_pixel4 = (0, 0, 0)
                new_img_pixel5 = (0, 0, 0)
                new_img_pixel6 = (0, 0, 0)
                if new_img_pixel(x == 0, y == 0):
                    new_r1 = (new_img_pixel(x + 1, y).red + new_img_pixel(x + 1, y + 1).red + new_img_pixel(x, y + 1).red+new_img_pixel(x,y).red) // 4
                    new_b1 = (new_img_pixel(x + 1, y).blue + new_img_pixel(x + 1, y + 1).blue + new_img_pixel(x, y + 1).blue+new_img_pixel(x,y).green) // 4
                    new_g1 = (new_img_pixel(x + 1, y).green + new_img_pixel(x + 1, y + 1).green + new_img_pixel(x, y + 1).green+new_img_pixel(x,y).green) // 4
                    new_img_pixel1=new_r1+new_g1+new_b1
                elif new_img_pixel(x==0,y == y):
                    new_r2 = (new_img_pixel(x + 1, y).red + new_img_pixel(x + 1, y + 1).red + new_img_pixel(x, y + 1).red+new_img_pixel(x,y).red) // 4
                    new_b2 = (new_img_pixel(x + 1, y).blue + new_img_pixel(x + 1, y + 1).blue + new_img_pixel(x, y + 1).blue+new_img_pixel(x,y).blue) // 4
                    new_g2 = (new_img_pixel(x + 1, y).green + new_img_pixel(x + 1, y + 1).green + new_img_pixel(x,y+1).green+new_img_pixel(x,y).green)//4
                    new_img_pixel2=new_g2+new_b2+new_r2
                elif new_img_pixel(x==x,y==0):
                    new_r3 = (new_img_pixel(x + 1, y).red + new_img_pixel(x + 1, y + 1).red + new_img_pixel(x, y + 1).red+new_img_pixel(x,y).red) // 4
                    new_b3 = (new_img_pixel(x + 1, y).blue + new_img_pixel(x + 1, y + 1).blue + new_img_pixel(x, y + 1).blue+new_img_pixel(x,y).blue) // 4
                    new_g3 = (new_img_pixel(x + 1, y).green + new_img_pixel(x + 1, y + 1).green + new_img_pixel(x,y + 1).green+new_img_pixel(x,y).green) // 4
                    new_img_pixel3 = new_g3 + new_b3 + new_r3
                elif new_img_pixel(x==0,y!=0):
                    new_r4 = (new_img_pixel(x+1,y).red+new_img_pixel(x+1,y+1).red+new_img_pixel(x,y-1).red+new_img_pixel(x,y+1).red+new_img_pixel(x+1,y-1).red+new_img_pixel(x,y).red)//6
                    new_b4 = (new_img_pixel(x+1,y).blue+new_img_pixel(x+1,y+1).blue+new_img_pixel(x,y-1).blue+new_img_pixel(x,y+1).blue+new_img_pixel(x+1,y-1).blue+new_img_pixel(x,y).blue)//6
                    new_g4 = (new_img_pixel(x+1,y).green+new_img_pixel(x+1,y+1).green+new_img_pixel(x,y-1).green+new_img_pixel(x,y+1).green+new_img_pixel(x+1,y-1).green+new_img_pixel(x,y).green)//6
                    new_img_pixel4 = new_g4+new_b4+new_r4
                elif new_img_pixel(x!=0,y==0):
                    new_r5 = (new_img_pixel(x+1,y+1).red+new_img_pixel(x,y+1).red+new_img_pixel(x-1,y).red+new_img_pixel(x+1,y).red+new_img_pixel(x-1,y+1).red+new_img_pixel(x,y).red)//6
                    new_b5 = (new_img_pixel(x+1,y+1).blue+new_img_pixel(x,y+1).blue+new_img_pixel(x-1,y).blue+new_img_pixel(x+1,y).blue+new_img_pixel(x-1,y+1).blue+new_img_pixel(x,y).blue)//6
                    new_g5 = (new_img_pixel(x+1,y+1).red+new_img_pixel(x,y+1).green+new_img_pixel(x-1,y).green+new_img_pixel(x+1,y).green+new_img_pixel(x-1,y+1).green+new_img_pixel(x,y).green)//6
                    new_img_pixel5=new_g5+new_b5+new_r5
                else:
                    new_r6=(new_img_pixel(x+1,y).red+new_img_pixel(x+1,y+1).red+new_img_pixel(x+1,y-1).red+new_img_pixel(x,y+1).red+new_img_pixel(x,y-1).red+new_img_pixel(x,y).red+new_img_pixel(x-1,y).red+new_img_pixel(x-1,y-1).red+new_img_pixel(x-1,y+1).red)//9
                    new_b6=(new_img_pixel(x+1,y).blue+new_img_pixel(x+1,y+1).blue+new_img_pixel(x+1,y-1).blue+new_img_pixel(x,y+1).blue+new_img_pixel(x,y-1).blue+new_img_pixel(x,y).blue+new_img_pixel(x-1,y).blue+new_img_pixel(x-1,y-1).blue+new_img_pixel(x-1,y+1).blue)//9
                    new_g6=(new_img_pixel(x+1,y).green+new_img_pixel(x+1,y+1).green+new_img_pixel(x+1,y-1).green+new_img_pixel(x,y+1).green+new_img_pixel(x,y-1).green+new_img_pixel(x,y).green+new_img_pixel(x-1,y).green+new_img_pixel(x-1,y-1).green+new_img_pixel(x-1,y+1).green)//9
                    new_img_pixel6 =new_g6+new_b6+new_r6
                new_img= new_img_pixel1 +new_img_pixel2+new_img_pixel3+new_img_pixel4+new_img_pixel5+new_img_pixel6

    return new_img


def main():

    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
