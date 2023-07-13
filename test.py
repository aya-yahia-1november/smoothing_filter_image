import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpg")

averaging=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bil=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("img",img)
cv2.imshow("aver",averaging)
cv2.imshow("gblur",gblur)
cv2.imshow("median",median)
cv2.imshow("bil",bil)
cv2.waitKey(0)
cv2.destroyAllWindows()
