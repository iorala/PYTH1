#
#
# Copyright 2021 Andreas la Roi, Fabian Introvigne, Michael Schlotter, Alexander van Schie, Nadine Christen, Juliane Streitberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
# Hausaufgabe Turtle
# Buchstaben zeichnen
import turtle
from turtle import Screen 

# Wir schreiben Python:
# Jede Gruppe schreibt einen Buchstaben (P-Y-T-H-O-N)
# Der Buchstabe muss innerhalb eines 300x400px Rahmens bleiben.
# Zeichnen Sie diesen  Rahmen mit folgender Zeile:
# turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90);turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90)
# Der Zeiger muss zum Schluss unten rechts, nach rechts zeigend stehen.
# Benutzen Sie keine relative Bewegungsbefehle (z.B.: home())
# Verpacken Sie Ihren Code in eine Funktion:

#
# Geschwindigkeit einstellen und cursor verstecken
#
turtle.speed(20)
#turtle.cursor(hide)
screen=Screen()
screen.setup(1700, 600)
#
# An den linken Rand springen
#
turtle.penup()
turtle.lt(180)
turtle.fd(900)
turtle.lt(90)
turtle.fd(200)
turtle.lt(90)
turtle.pendown()

def gruppe_JAMFAN_P():


    #
    # Rechteck zeichnen
    #

    turtle.pencolor("light green")
    turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90);turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90)
    turtle.pencolor("black")

    ## P zeichnen

    turtle.penup()
    turtle.fd(70)
    turtle.lt(90)
    turtle.fd(10)
    turtle.rt(90)
    turtle.pendown()
    turtle.fillcolor("black")

    ## Erste Form
    turtle.begin_fill()
    turtle.lt(20)
    turtle.fd(65)
    turtle.lt(70)
    turtle.fd(290)
    turtle.lt(120)
    turtle.fd(70)
    turtle.lt(60)
    turtle.fd(277)
    turtle.end_fill()

    ## Zweite Form
    turtle.penup()
    turtle.lt(180)
    turtle.fd(110)
    turtle.lt(70)
    turtle.fd(20)
    turtle.lt(180)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.fd(120)
    turtle.lt(40)
    turtle.fd(80)
    turtle.lt(70)
    turtle.fd(240)
    turtle.lt(80)
    turtle.fd(175)
    turtle.lt(80)
    turtle.fd(60)
    turtle.lt(100)
    turtle.fd(135)
    turtle.rt(80)
    turtle.fd(165)
    turtle.rt(110)
    turtle.fd(116)
    turtle.lt(90)
    turtle.fd(55)
    turtle.end_fill()
    #turtle.hideturtle()
    turtle.penup()
    turtle.lt(20)
    turtle.fd(127)
    turtle.lt(90)
    ## Für Kerning anpassen (248 ist am ende der Box, 188 ist ohne Abstand) 
    turtle.fd(188)
    ##/Kerning
   

gruppe_JAMFAN_P()
gruppe_JAMFAN_P()
gruppe_JAMFAN_P()
gruppe_JAMFAN_P()
gruppe_JAMFAN_P()
gruppe_JAMFAN_P()
turtle.exitonclick()