"""15. Напишите инструкции черепашьей графики, чтобы нарисовать квадрат со стороной
100 пикселов и круг в центре квадрата. Радиус круга должен составить 80 пикселов.
Круг должен быть заполнен красным цветом. (Квадрат не должен быть заполнен
цветом.)"""


import turtle

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.showturtle()
turtle.left(90)
turtle.penup()
turtle.forward(30)
turtle.right(90)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.end_fill()
turtle.mainloop()