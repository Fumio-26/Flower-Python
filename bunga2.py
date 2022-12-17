import turtle as te
import colorsys as cs
te.setup(600,600)
te.screensize(100)
te.speed(0)
te.width(2)
te.tracer(100)
te.bgcolor("black")
for y in range (25):
    for i in range (15):
        te.color(cs.hsv_to_rgb(y/15,i/25,1))
        te.right(90)
        te.circle(200-y*4,90)
        te.left(90)
        te.circle(200-y*4,90)
        te.right(180)
        te.circle(50,24)
te.hideturtle()
te.done