import cv2
import matplotlib.pyplot as plt
import numpy as np
path=input("enter path: ")
img=cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)
angle=float(input("enter angle in radians"))
h,w=img.shape[:2]
M=cv2.getRotationMatrix2D((w / 2,h / 2),angle,1)
out=cv2.warpAffine(img,M,(w,h))
print("rotation matrix:",M.round(3))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("original")
plt.subplot(1,2,2)
plt.imshow(out)
plt.title("rotated")
plt.show()