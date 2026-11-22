import cv2
import matplotlib.pyplot as plt
gray = cv2.imread("su.jpg.jpg",0)

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.imshow(gray,cmap="gray")
plt.title("original")

for i,T in enumerate([50,100,150]):
  _,th=cv2.threshold(gray,T,255,cv2.THRESH_BINARY)
  plt.subplot(2,3,i+2)
  plt.imshow(th,cmap="grey")
  plt.title("global t"+ str(T))


band=cv2.inRange(gray,100,180)
plt.subplot(2,3,5)
plt.imshow(band,cmap="gray")
plt.title("intensity threshold")

plt.subplot(2,3,6)
plt.hist(gray.ravel(),bins=256,range=(0,256))
plt.title("intensity histogram")
plt.show()