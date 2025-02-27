from turtle import *
from math import sqrt
def draw_triangle(reverse=+1,length=50):
    left(60)
    fd(length)
    left(-120*reverse)
    fd(length)
    left(-120*reverse)
    fd(length)
color('blue')

up()
seth(-145)
fd(200)
down()
seth(0)
begin_fill()
draw_triangle(+1,180)
end_fill()
seth(90)
up()
fd(60*sqrt(3))
down()
seth(-120)
begin_fill()
draw_triangle(-1,180)
end_fill()
