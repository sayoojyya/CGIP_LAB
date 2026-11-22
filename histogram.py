import cv2
import matplotlib.pyplot as plt

path=input("enter path")
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eq=cv2.equalizeHist(gray)
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.imshow(gray,cmap="gray")
plt.title("original")

plt.subplot(2,2,2)
plt.hist(gray.ravel(),bins=256,range=(0,256))
plt.title("original histogram")

plt.subplot(2,2,3)
plt.imshow(eq,cmap="gray")
plt.title("equilized")

plt.subplot(2,2,4)
plt.hist(eq.ravel(),bins=256,range=(0,256))
plt.title("equilized histogram")

plt.show()