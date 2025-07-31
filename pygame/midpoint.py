import pygame
import sys
import math

def midpoint(x1,y1,r):
    
    x,y = 0,r
    p = 1 - r
    while(x <= y):
        screen.set_at(((x1+x),(y1+y)),(0,245,67))
        screen.set_at(((x1-x),(y1+y)),(0,245,67))
        screen.set_at(((x1+x),(y1-y)),(0,245,67))
        screen.set_at(((x1-x),(y1-y)),(0,245,67))
        screen.set_at(((x1+y),(y1+x)),(0,245,67))
        screen.set_at(((x1-y),(y1+x)),(0,245,67))
        screen.set_at(((x1+y),(y1-x)),(0,245,67))
        screen.set_at(((x1-y),(y1-x)),(0,245,67))

        if(p < 0):
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*(x-y) + 1
        x += 1
    pygame.display.flip()
pygame.init()
w,h = 800,500
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Midpoint Circle")
BLACK,WHITE = (0,0,0),(255,255,255)

x1 = int(input("Enter the value of center(x1):"))
y1 = int(input("Enter the value of center(y1):"))
r = int(input("Enter the radius:"))

midpoint(x1,y1,r)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()