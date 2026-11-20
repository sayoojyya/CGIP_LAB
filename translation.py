import numpy as np
import matplotlib.pyplot as plt
tx,ty=map(int,input("Enter translation factor tx and ty: ").split())
pts=np.array([[1,1],[5,1],[3,4],[1,1]])
new=pts+[tx,ty]
print ("Original points:\n",pts)
print("Translated points:\n",new)
plt.plot(pts[:,0], pts[:,1], 'ro-', label='Original')
plt.plot(new[:,0], new[:,1], 'bo-', label='Translated')
plt.legend()
plt.grid(True)
plt.show()