import matplotlib.pyplot as plt
import numpy as np

pts=np.array([[1,1],[5,1],[3,4],[1,1]])
angle=float(input("enter angle in degrees: "))
t=np.radians(angle)
R=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

new=(R @ pts.T).T
print("original points\n",R.round(2))
print("rotated points,new:\n",new.round(2))
plt.plot(pts[:,0],pts[:,1],'ro-',label="original")
plt.plot(new[:,0],new[:,1],'bo-',label="rotated")
plt.legend()
plt.grid(True)
plt.show()