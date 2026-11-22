import numpy as np
import cv2
import matplotlib.pyplot as plt
path=input("Enter a path: ")
img=cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)

h,w=img.shape[:2]
tx,ty=map(int,input("enter tx,ty:").split())
M=np.float32([[1,0,tx],[0,1,ty]])

out=cv2.warpAffine(img,M,(w,h))
print("translation matrix=:",M)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(out)
plt.title("translated")

plt.show()