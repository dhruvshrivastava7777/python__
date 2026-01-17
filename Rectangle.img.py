# import cv2
# image=cv2.imread("./team.png")   

# cv2.rectangle(image, (100,100), (250,200), (0,255,0), 5)
# cv2.imshow(" Image", image)
# cv2.waitKey(0)
import cv2
import cv2.data


modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)

image= cv2.imread("./team.png")
faces = model.detectMultiScale(image, 1.3, 6  )
for face in faces:
    x, y, w, h = face
    image= cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("Faces",image)
cv2.waitKey(0)