import cv2
import numpy as np
import matplotlib.pyplot as plt

path=input("enter path")
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kx=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
ky=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

gx=cv2.filter2D(gray,cv2.CV_64F,kx)
gy=cv2.filter2D(gray,cv2.CV_64F,ky)

edges=np.sqrt(gx**2 + gy**2)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(gray,cmap="gray")
plt.title("original")

plt.subplot(1,4,2)
plt.imshow(np.abs(gx),cmap="gray")
plt.title("prewitt X")


plt.subplot(1,4,3)
plt.imshow(np.abs(gy),cmap="gray")
plt.title("prewitt y")

plt.subplot(1,4,4)
plt.imshow(edges,cmap="gray")
plt.title("prewitt edge")

plt.show()
