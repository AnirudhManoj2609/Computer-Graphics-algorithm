import matplotlib.pyplot as plt

def ddaa(x1,x2,y1,y2):
    dx,dy = x2-x1,y2-y1
    steps = max(round(abs(dx)),round(abs(dy)))
    X,Y = [round(x1)],[round(y1)]
    for i in range(steps):
        x1 += dx/steps
        y1 += dy/steps
        X.append(round(x1))
        Y.append(round(y1))
    X.append(x2)
    Y.append(y2)

    plt.figure(figsize=(10,10))
    plt.scatter(X,Y,color="red")
    plt.title("DDA")
    plt.show()
x1 = float(input("Enter the value of x1:"))
y1 = float(input("Enter the value of y1:"))
x2 = float(input("Enter the value of x2:"))
y2 = float(input("Enter the value of y2:"))

ddaa(x1,x2,y1,y2)
