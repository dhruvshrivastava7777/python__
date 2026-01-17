import cv2
image = cv2.imread("./team.png")
new_image = cv2.resize(image, (1400, 1000))

cv2.imshow(" Image", image)
cv2.waitKey(0)
