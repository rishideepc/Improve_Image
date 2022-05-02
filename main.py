import cv2

image_1= cv2.imread("image_3.jpeg")   

image_1= cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
image_1= cv2.resize(image_1, (560, 900))

_, result= cv2.threshold(image_1, 20, 250, cv2.THRESH_BINARY)

adaptive_result= cv2.adaptiveThreshold(image_1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 41, 5)

cv2.imshow("result", result)
cv2.imshow("original", image_1)
cv2.imshow("adaptive", adaptive_result)

cv2.waitKey(0)
