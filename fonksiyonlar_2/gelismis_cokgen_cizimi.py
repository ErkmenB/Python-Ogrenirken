import turtle
import random
#program cokgen cizer. x ve koordinatlarından başlar. dolgu olup olmayacağı belirlenir(varsayılan= False)

def Cokgen(kenarsayisi,uzunluk,x,y,renk="black",dolgu=False):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.color(renk)
    if dolgu:
        turtle.begin_fill()
    for i in range(kenarsayisi):
        turtle.forward(uzunluk)
        turtle.left(360//kenarsayisi)
    if dolgu:
        turtle.end_fill()
        turtle.hideturtle()
        turtle.tracer(0)

Cokgen(3,30,10,10)
Cokgen(4,30,50,50,"blue")
Cokgen(5,30,100,100,"red",True)
turtle.update()
turtle.exitonclick()