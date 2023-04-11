import cv2

#https://github.com/opencv/opencv/tree/master/data/haarcascades #Модели нейронных сетей

img = cv2.imread('images/face1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=4)#scaleFactor 1.1 min, надо играться для разных фото

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow("Result", img)
cv2.waitKey(0)
