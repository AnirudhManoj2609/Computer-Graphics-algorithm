import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1
    p = 2*dy - dx

    X = [x]
    Y = [y]

    for _ in range(dx):
        x += 1
        if p < 0:
            p = p + 2*abs(dy)
        else:
            y = y + (dy/abs(dy))*1
            p = p + 2*(dy - dx)
        X.append(x)
        Y.append(y)

    plt.figure(figsize=(10, 5))
    plt.scatter(X, Y, color="red")
    plt.plot(X, Y, linestyle='dashed', color='blue')
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.grid(True)
    plt.show()


x1 = int(input("Enter the value of starting point x1: "))
y1 = int(input("Enter the value of starting point y1: "))
x2 = int(input("Enter the value of end point x2: "))
y2 = int(input("Enter the value of end point y2: "))


if x2 < x1:
    x1, x2 = x2, x1
    y1, y2 = y2, y1

bresenham(x1, y1, x2, y2)
