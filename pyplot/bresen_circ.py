import matplotlib.pyplot as plt

def bresenham(x1,y1,r):
    
    x,y = 0,r
    p = 3 - 2*r
    X,Y = [],[]
    while(x <= y):
        X.append(x1+x),Y.append(y1+y)
        X.append(x1-x),Y.append(y1+y)
        X.append(x1+x),Y.append(y1-y)
        X.append(x1-x),Y.append(y1-y)
        X.append(x1+y),Y.append(y1+x)
        X.append(x1-y),Y.append(y1+x)
        X.append(x1+y),Y.append(y1-x)
        X.append(x1-y),Y.append(y1-x)
        if(p < 0):
            p = p + 4*x + 6
        else:
            y -= 1
            p = p + 4*(x-y) + 10
        x += 1

    plt.figure(figsize=(20,10))
    plt.scatter(X,Y,color="red")
    plt.title("Bresenham")
    plt.show()

x1 = int(input("Enter the value of center(x1):"))
y1 = int(input("Enter the value of center(y1):"))
r = int(input("Enter the radius:"))

bresenham(x1,y1,r)