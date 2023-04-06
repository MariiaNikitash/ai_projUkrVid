import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8') #оздает матрицу с нулями

# RGB - standard
# BGR - формат в OpenCV

#photo[10:150, 200:280] = 119, 201, 105 #1 это границы 2 - цвета, in google- color pickr and change place 1 n 3

cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=cv2.FILLED)

cv2.line(photo, (0, photo.shape[0]// 2), (photo.shape[1], photo.shape[0]// 2), (119, 201, 105), thickness=3)

cv2.circle(photo, (photo.shape[1]// 2, photo.shape[0]// 2), 100, (119, 201, 105), thickness=cv2.FILLED)

cv2.putText(photo, 'Mashka', (160, 190), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)





