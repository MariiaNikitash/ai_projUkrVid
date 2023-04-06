'''
import cv2
import numpy as np

img = cv2.imread('images/PracImage.jpg')

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) #makes image twice smaller
img = cv2.GaussianBlur(img, (9, 9), 0)#размытие на фото только нечетные/odds otherwise error
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #makes one layer, only grey

img = cv2.Canny(img, 200, 200) #указывает котнуры, бинарный формат, but at first COLOR_BGR2GRAY меньше число - больше четкость

#img[0:100, 0:150]) #обрезает картинку, начало на 00 в левом верхнем углу

kernel = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1) #kernel кол-во точек

img = cv2.erode(img, kernel, iterations=1)


cv2.imshow('Result', img)

print(img.shape)

cv2.waitKey(0) # 0 i картинка показывается бесконечно




#capture = cv2.VideoCapture(0)
#capture.set(3, 500)
#capture.set(4, 300)

#while True:
#    success, img = capture.read()
#    cv2.imshow('Result', img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
'''
