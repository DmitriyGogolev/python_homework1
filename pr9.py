"""14. Напишите инструкции черепашьей графики, чтобы нарисовать квадрат со стороной
100 пикселов и заполненный синим цветом. """
import turtle
turtle.hideturtle()
turtle. fillcolor ( 'blue')
turtle.begin_fill()
turtle.forward(100)
turtle. left ( 90)
turtle.forward(100)
turtle. left ( 90)
turtle.forward(100)
turtle. left ( 90)
turtle.forward(100)
turtle.end_fill()
turtle.mainloop()