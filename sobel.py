import cv2
import numpy as np
import matplotlib.pyplot as plt

path=input("enter path")
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ky=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
kx=np.array([[-1,0,1],[0,0,0],[-2,0,2]])

gx=cv2.filter2D(gray,cv2.CV_64F,kx)
gy=cv2.filter2D(gray,cv2.CV_64F,ky)

edges=np.sqrt(gx ** 2+gy ** 2)

plt.figure(figsize=(12,8))
plt.subplot(1,4,1)
plt.imshow(gray,cmap="gray")
plt.title("original")

plt.subplot(1,4,2)
plt.imshow(np.abs(gx),cmap="gray")
plt.title("sobel x")

plt.subplot(1,4,3)
plt.imshow(np.abs(gy),cmap="gray")
plt.title("sobel y")

plt.subplot(1,4,4)
plt.imshow(edges,cmap="gray")
plt.title("sobel")

plt.show()