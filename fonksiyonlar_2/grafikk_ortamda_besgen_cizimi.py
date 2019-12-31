# turtle modu kullanılarak beşgen çizimi
import turtle
import random
#turtle modülü programa ekleniyor.
def besgen(sides,length,x,y,color):
#besgen adı altında bir fonksiyon tanımladık.

 turtle.penup()
 turtle.setposition(x,y)
 turtle.pendown()
 turtle.color(color)
 turtle.begin_fill()

 for i in range(sides):
    turtle.forward(length)
    turtle.left(360//sides)
    turtle.end_fill()

besgen(5,100,50,50,"blue")

