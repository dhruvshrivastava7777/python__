import cv2
import cv2.data
from random import randint                                
modelpath=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
model=cv2.CascadeClassifier(modelpath)
# image=cv2.imread("./team.png")
# faces=model.detectMultiScale(image,1.3,5)
# for face in faces:
#     x,y,w,h = face

#     red= randint(0,255)
#     green= randint(0,255)
#     blue= randint(0,255)
#     image=cv2.rectangle(image,(x,y),(x+w,y+h),(red,green,blue),3)
# cv2.imshow("Faces",image)
# cv2.waitKey(0) 

camera = cv2.VideoCapture(0)

while True:
    status,frame = camera.read()
    faces = model.detectMultiScale(frame,1.3,5)
    for face in faces:
        x,y,w,h = face

        frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Faces",frame)
    if cv2.waitKey(1) == ord('q'):
        break
