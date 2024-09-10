from turtle import *
tracer(0)
m = 50
screensize(1920,1080)
left(90)
right(45)
for i in range(7):
    forward(5*m)
    right(45)
    forward(10*m)
    right(135)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        setpos(x*m, y*m)
        dot(5)
done()