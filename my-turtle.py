import turtle
turtle.up()
turtle.seth(-145)
turtle.fd(200)
turtle.down()
turtle.pensize(2)
turtle.color('purple')
turtle.seth(90)

for i in range(300,5,-10):
   turtle.fd(i)
   turtle.seth(0)
   turtle.fd(i)
   turtle.seth(-90)
   turtle.fd(i-5)
   turtle.seth(180)
   turtle.fd(i-5)
   turtle.seth(90)
   
   

