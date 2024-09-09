import turtle
import math


class Clock:
    # konstruktor
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.radius = 300

        # a mutatok szogeinek beallitasa, perc & oranal eltolas is van (+ ido/60 * fok)
        self.secondAngle = second * 6
        self.minuteAngle = (minute * 6) + (second / 60 * 6)
        self.hourAngle = (hour % 12) * 30 + (minute / 60 * 30)

    # fgv. amit meghivsz a mainbol
    def showTime(self):
        self.createClock()
        self.createNums()
        self.drawHandles()
        turtle.done()

    # ora base megrajzolasa
    def createClock(self):
        turtle.reset()
        turtle.speed(0)

        turtle.penup()
        turtle.goto(0, -self.radius)

        turtle.pendown()
        turtle.circle(self.radius)

    # szamok es pontok megrajzolasa, x & y koordinata szogfv-ekkel van
    def createNums(self):
        turtle.penup()
        for second in range(0, 60):
            angle = math.radians(360 / 60 * second)
            x = self.radius * 0.85 * math.sin(angle)
            y = self.radius * 0.85 * math.cos(angle)
            turtle.goto(x, y)

            if second % 5 != 0:
                turtle.pendown()
                turtle.circle(3)
                turtle.penup()

        for hour in range(1, 13):
            angle = math.radians(360 / 12 * hour)
            x = self.radius * 0.85 * math.sin(angle)
            y = self.radius * 0.85 * math.cos(angle) - 7
            turtle.goto(x, y)
            turtle.write(str(hour), font=("Times New Roman", 14, "bold"), align="center")

    # a mutatok megrajzolasa
    def drawHandles(self):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90)
        turtle.right(self.hourAngle)
        turtle.pendown()
        turtle.forward(150)

        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90)
        turtle.right(self.minuteAngle)
        turtle.pendown()
        turtle.forward(190)

        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90)
        turtle.right(self.secondAngle)
        turtle.pendown()
        turtle.forward(240)
