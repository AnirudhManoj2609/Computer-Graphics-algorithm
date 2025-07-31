import pygame
import sys
import math

def bresenham(x1, x2, y1, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1
    p = 2*dy - dx
    k = 0
    if dx == 0:
        k = dy
    else:
        k = dx
    for _ in range(int(k)):
        if dx != 0:
            x += 1
        if p < 0:
            p = p + 2*abs(dy)
        else:
            y = y + (dy/abs(dy))*1
            p = p + 2*(dy - dx)
        screen.set_at((round(x),round(y)),(0,245,67))
        
    pygame.display.flip()
    

pygame.init()
w,h = 800,500
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Bresenham Line")
BLACK,WHITE = (0,0,0),(255,255,255)
x1 = float(input("Enter the value of x1:"))
y1 = float(input("Enter the value of y1:"))
x2 = float(input("Enter the value of x2:"))
y2 = float(input("Enter the value of y2:"))

bresenham(x1,x2,y1,y2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()