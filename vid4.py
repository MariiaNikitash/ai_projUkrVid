import cv2
import numpy as np



img = cv2.imread('images/PracImage.jpg')

new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (230, 111, 148), 1)

print(con)

'''
#img = cv2.flip(img, -1)  

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1) #rotation
    return cv2.warpAffine(img_param, mat, (width, height) )

# img = rotate(img, 90) #90 is angle of rotation

def transform(img_param, x, y ):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0] ))

img = transform(img, 30, 200) #30 смещение по х, 200 смещение по у
'''


cv2.imshow("Result", new_img)

cv2.waitKey(0)











'''
cap = cv2.VideoCapture('videos/kyivV.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    #img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) #makes image twice smaller
    img = cv2.GaussianBlur(img, (9, 9), 0)#размытие на фото только нечетные/odds otherwise error
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    img = cv2.Canny(img, 100, 100)#котнуры четче 



    kernel = np.ones((5,5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1) 

    img = cv2.erode(img, kernel, iterations=1)


    cv2.imshow('Result', img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
