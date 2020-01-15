# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-13 10:14 '

import tesserocr
from PIL import Image
image = Image.open('blog2020.png')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)
