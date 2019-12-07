# coding=UTF-8

from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('System/Library/Fonts/Supplemental/Arial.ttf',
                                size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

    return 0


if __name__ == '__main__':
    image = Image.open(
        '/Users/lixiuwen/Library/Mobile Documents/com~apple~CloudDocs/mac备份/1x/资源 2.png'
    )
    add_num(image)
