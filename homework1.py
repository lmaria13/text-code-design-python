
# task 2

from drawbot_skia.drawbot import rect, saveImage
x = 50
y = 50
step = 200
for i in range(9):
    for j in range (9):
        rect(x, y, 100, 100)
        y = y + step
    y = 50
    x = x + step

saveImage("task2.pdf")


# task 3
# фантазии питона на тему конструктивизма

from drawbot_skia.drawbot import rect, polygon, polygon, saveImage, fill, stroke, strokeWidth
fill(None)
stroke(0, 0, 0)
strokeWidth(10)


fill(1, 0, 0)

x = 50
y = 50
step = 200
for i in range(9):
    for j in range (9):
        rect(x, y, 100, 100)
        y = y + step
    y = 50
    x = x + step
fill(None)
stroke(0, 0, 1)
strokeWidth(50)

saveImage("task3.pdf")