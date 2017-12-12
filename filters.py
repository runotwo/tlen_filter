from copy import deepcopy

from PIL import Image, ImageDraw


def make_grey(image):
    copy = deepcopy(image)
    draw = ImageDraw.Draw(copy)
    width = copy.size[0]
    height = copy.size[1]
    pix = copy.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            med = (a + b + c) // 3
            draw.point((i, j), ((a + 3 * med) // 4, (b + 3 * med) // 4, (c + 3 * med) // 4, 255))
    return copy


def make_white_eyes(image, eyes_list):
    copy = deepcopy(image)
    draw = ImageDraw.Draw(copy)
    pix = copy.load()
    for (xmin, ymin, xmax, ymax) in eyes_list:
        w = xmax - xmin
        h = ymax - ymin
        draw.ellipse((xmin+w/4, ymin+h/4, xmax-w/4, ymax-h/4), fill=(255, 255, 255, 126))
    return copy


def make_tlen(image, tlen_image):
    copy = deepcopy(image)
    tlen_copy = deepcopy(tlen_image)
    width = copy.size[0]
    height = copy.size[1]
    tlen_copy = tlen_copy.resize((width, height))
    draw = ImageDraw.Draw(tlen_copy, 'RGBA')
    pixels = tlen_copy.load()
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            draw.point((i, j), fill=(a, b, c, 100))
    return Image.alpha_composite(copy, tlen_copy)
