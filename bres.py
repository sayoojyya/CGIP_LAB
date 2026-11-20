import matplotlib.pyplot as plt
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

dx=x2-x1
dy=y2-y1
p=2*dy-dx
x=x1
y=y1
px=[]
py=[]
while x<=x2:
    px.append(x)
    py.append(y)
    x+=1
    if p<0:
        p+=2*dy
    else:
        y+=1
        p+=2*dy-2*dx
print(px,py)
    
plt.plot(px,py,'ro-')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
