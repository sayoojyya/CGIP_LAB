import matplotlib.pyplot as plt
x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))

dx= x2 - x1
dy= y2 - y1

steps= max(abs(dx),abs(dy))
if steps==0:
    print("both are same")
else:
    x_inc=dx/steps
    y_inc=dy/steps

    x=x1
    y=y1

    x_points=[]
    y_points=[]

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))

        x=x+x_inc
        y=y+y_inc
    plt.plot(x_points,y_points,'ro-')
    plt.title("DDA line drawing algorithm")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(True)
    plt.show()