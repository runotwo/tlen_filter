import cv2


def eye_detector(img_name):
    eye_cascade = cv2.CascadeClassifier('eye.xml')
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    coords = []
    for (x, y, w, h) in eyes:
        coords.append((x, y, x + w, y + h))
    return coords

