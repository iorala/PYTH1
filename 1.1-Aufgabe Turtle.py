# Hausaufgabe Turtle
# Buchstaben zeichnen
import turtle
import time

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
turtle.speed(3)
turtle.shape("turtle")
time.sleep(5)

#
# An den linken Rand springen
#
turtle.penup()
turtle.lt(180)
turtle.fd(400)
turtle.lt(90)
turtle.fd(200)
turtle.lt(90)
turtle.pendown()

#
# Rechteck zeichnen
#

turtle.pencolor("light green")
turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90);turtle.fd(300);turtle.lt(90);turtle.fd(400);turtle.lt(90)
turtle.pencolor("black")

## P zeichnen

turtle.penup()
turtle.fd(30)
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
turtle.fd(100)
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
turtle.fd(250)
turtle.lt(80)
turtle.fd(175)
turtle.lt(80)
turtle.fd(60)
turtle.lt(100)
turtle.fd(135)
turtle.rt(80)
turtle.fd(175)
turtle.rt(110)
turtle.fd(116)
turtle.lt(90)
turtle.fd(49)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

