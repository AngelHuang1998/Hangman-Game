from turtle import *
import random

speed(0)

def people():
    """ 繪製人 """
    penup()
    goto(-220, 50)
    pendown()
    right(90)
    forward(75)
    back(75)
    left(90)
    circle(25)
    right(90)
    forward(25)
    right(135)
    forward(50)
    back(50)
    right(90)
    forward(50)
    back(50)
    right(135)
    forward(50)
    right(30)
    forward(50)
    back(50)
    left(60)
    forward(50)
    left(60)


def draw_rectangle(x, y, width, height, color_fill=None):
    """ 繪製矩形（可選填充顏色），方便畫車子時用到"""
    penup()
    goto(x, y)
    pendown()
    if color_fill:
        color(color_fill)
        begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    if color_fill:
        end_fill()


def car(opportunity):
    """ 繪製行駛中的車 """
    pensize(5)
    offset = opportunity * 60  
    draw_rectangle(-140 + offset, -70, 200, 200, "white")  #遮底圖的白畫布
    draw_rectangle(-200 + offset, -50, 200, 50, "green")    # 車身
    draw_rectangle(-170 + offset, 0, 140, 38, "orange")     # 車窗

    penup()
    goto(-150 + offset, -60)
    pendown()
    color("gray")
    circle(20)  #輪胎

    penup()
    goto(-50 + offset, -60)
    pendown()
    circle(20)


def last_car():
    """ 繪製最後撞到人的車 """
    pensize(5)
    draw_rectangle(-140, -70, 200, 200, "white")   #遮底圖的白畫布
    draw_rectangle(-190, -50, 200, 50, "green")    # 車身
    draw_rectangle(-160, 0, 140, 38, "orange")     # 車窗

    penup()
    goto(-140, -60)
    pendown()
    color("gray")
    circle(20)

    penup()
    goto(-40, -60)
    pendown()
    circle(20)


def draw_blood_splatter():
    """ 繪製血跡噴濺 """
    color("red")
    hideturtle()
    penup()
    goto(-200, 0)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

    for _ in range(30): 
        angle = random.randint(0, 360)
        distance = random.randint(30, 150)
        size = random.randint(1, 3)

        penup()
        setheading(angle)
        forward(distance)
        pendown()
        begin_fill()
        circle(size)
        end_fill()
        penup()
        goto(-200, 0)
