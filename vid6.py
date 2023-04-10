import cv2
import numpy

img = numpy.zeros((350, 350), dtype='uint8')

circle = cv2.circle(img.copy(), (0, 0), 50, 255, -1)
square =  cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)


cv2.imshow("Result", circle)
cv2.waitKey(0)