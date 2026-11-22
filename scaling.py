import numpy as np
import matplotlib.pyplot as plt
pts=np.array([[1,2],[1,5],[3,4],[1,2]])
sx,sy=map(int,input("enter sx sy:").split())
S=np.array([[sx,0],[0,sy]])
new=(S @ pts.T).T
print("original points\n",pts)
print("scaled points,new:\n",new)
plt.plot(pts[:,0],pts[:,1],'ro-',label="original")
plt.plot(new[:,0],new[:,1],'bo-',label="scaled")
plt.legend()
plt.grid(True)
plt.show()