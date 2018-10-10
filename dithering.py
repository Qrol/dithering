from PIL import Image
import numpy as np

findClosestColor = lambda value: int(round(value/16.0))*16

image = Image.open('dragon.jpg')
imageData = np.asarray(image).copy()
for i, line in enumerate(imageData):
    for j, pixel in enumerate(line):
        oldPixel = pixel.copy()
        imageData[i][j] = np.array([findClosestColor(val) for val in pixel])
Image.fromarray(imageData).save('dragonReducedColor.jpg')
