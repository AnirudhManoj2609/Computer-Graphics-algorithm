import pygame
import sys
import math
def ddaa(x1,x2,y1,y2):
    dx,dy = x2 - x1,y2 - y1
    steps = max(round(abs(dx)),round(abs(dy)))

    for i in range(steps + 1):
        screen.set_at((round(x1),round(y1)),(0,245,67))
        x1 += dx/steps
        y1 += dy/steps
    pygame.display.flip()

pygame.init()
w,h = 800,500
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("DDA")
BLACK,WHITE = (0,0,0),(255,255,255)
x1 = float(input("Enter the value of x1:"))
y1 = float(input("Enter the value of y1:"))
x2 = float(input("Enter the value of x2:"))
y2 = float(input("Enter the value of y2:"))

ddaa(x1,x2+w/2,y1,y2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()