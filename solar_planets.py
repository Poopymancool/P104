import cv2

img = cv2.imread("solar-system.jpg")
rocket = img[120:360,400:500]

cv2.putText(img, "Sun", (100,50), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Mercury", (125,300), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Venus", (200,150), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Earth", (300,300), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Moon", (325,150), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Mars", (350,180), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Jupiter", (525,50), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Saturn", (700,100), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Uranus", (900,100), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Neptune", (1100,100), fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(0,0,255))
cv2.imshow("iemg", img)
cv2.imwrite("solar_systemwithnames.jpg", img)
cv2.waitKey(0)