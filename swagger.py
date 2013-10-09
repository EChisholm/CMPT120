import turtle as t
import random as r

def nthcircle(radius,n):
    for i in range(1,n):
        radius = radius*(i**.5)
        t.circle(radius)
        t.pencolor(r.randint(0,225),r.randint(0,225),r.randint(0,225))
        
t.colormode(255)
nthcircle(1,10)
