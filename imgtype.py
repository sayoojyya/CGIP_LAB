import cv2
import matplotlib.pyplot as plt
import numpy as np

path=input("enter image path: ")
img=cv2.imread(path)

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

print("RGB image shape:",rgb.shape)
print("gray image shape:",gray.shape)
print("binary image shape:",np.unique(binary))

plt.figure(figsize=(12,14))
plt.subplot(1,3,1)
plt.imshow(rgb)
plt.title("rgb")
plt.subplot(1,3,2)
plt.imshow(gray,cmap="gray")
plt.title("gray")
plt.subplot(1,3,3)
plt.imshow(binary,cmap="gray")
plt.title("binary")
plt.show()
