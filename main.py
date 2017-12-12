import os
from PIL import Image
from filters import make_grey, make_white_eyes, make_tlen
from detectors import eye_detector


def process(image_name):
    img = Image.open(image_name).convert('RGBA')
    tlen_img = Image.open('filt.png').convert('RGBA')
    eyes = eye_detector(image_name)
    img = make_white_eyes(img, eyes)
    img = make_grey(img)
    res = make_tlen(img, tlen_img)
    res.save("ans.png", "PNG")

if __name__ == '__main__':
    image_name = input('Your image:')
    if os.path.isfile(image_name):
        process(image_name)
    else:
        print(image_name)