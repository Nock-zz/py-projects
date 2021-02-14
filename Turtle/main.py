# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# from turtle import Screen, Turtle
#
# my_turtle = Turtle()
# my_screen = Screen()
# my_turtle.color('red', 'yellow')
#
# my_turtle.shape('triangle')
#
# print(type(my_turtle.pos()))
# print(dur(my_turtle.pos()))
#
# my_turtle.begin_fill()
# while True:
#     my_turtle.forward(200)
#     my_turtle.left(170)
#     if abs(my_turtle.pos()) < 1:
#         break
# my_turtle.end_fill()
#
# my_turtle.forward(300)
# for _ in range(5):
#     my_turtle.right(270)
#     my_turtle.forward(400)

# my_screen.exitonclick()
# my_screen.done()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Pokemon Website https://pokemondb.net/pokedex/game/x-y

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)




