import cv2
import numpy as np
import matplotlib.pyplot as plt

path=input("enter path")
img=cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)
sx,sy=map(float,input("enter sx,sy:").split())
out=cv2.resize(img,None,fx=sx,fy=sy)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.subplot(1,2,2)
plt.imshow(out)
plt.title("Scaled")
plt.show()