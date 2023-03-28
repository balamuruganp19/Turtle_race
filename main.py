from turtle import Turtle, Screen
import random

turtle_list = []

tim = Turtle("turtle")
tommy = Turtle("turtle")
johny = Turtle("turtle")
benny = Turtle("turtle")
turtle_list.append(tim)
turtle_list.append(tommy)
turtle_list.append(johny)
turtle_list.append(benny)

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput("Turtle Race", prompt="Who Will Win The Race")



def penup():
    tim.penup()
    tommy.penup()
    johny.penup()
    benny.penup()


def start():
    tim.color("red")
    tommy.color("yellow")
    johny.color("green")
    benny.color("blue")


def movement():
    tim.goto(x=-240, y=20)
    tommy.goto(x=-240, y=-20)
    johny.goto(x=-240, y=-60)
    benny.goto(x=-240, y=60)


def race():
    tim.forward(random.randint(2, 4))
    tommy.forward(random.randint(2, 4))
    johny.forward(random.randint(2, 4))
    benny.forward(random.randint(2, 4))


game_is_on = False
penup()
start()
movement()

if user_bet:
    game_is_on = True


while game_is_on:
    race()
    for i in turtle_list:
        if i.xcor() > 230:
            winning_color = i.pencolor()
            screen.textinput("Race Winner", f"Winner is {i.pencolor()}")
            if user_bet == winning_color:
                print(f"you are the Winner{winning_color}")
            else:
                print(f"You Lose The Game The winner is {winning_color}")
            game_is_on = False

screen.exitonclick()

#
#
# def forward():
#     tim.forward(50)
#
#
# def backward():
#     tim.backward(50)
#
#
# def clockwise():
#     tim.left(10)
#
#
# def counterclockwise():
#     tim.right(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=clockwise)
# screen.onkey(key="d", fun=counterclockwise)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def calculation(n1, n2, fun):
#     print(fun(n1, n2))
#
#
# calculation(2, 3, multiply)
# # print(result)
