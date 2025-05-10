# midterm review - assignment 1 - book club points

books_bought = int(input("How many books did you buy?"))

points = 0

# using match case (python switch equivalent)
# match books_bought:
#     case 1:
#         points = 6;
#     case 2:
#         points = 16;
#     case 3:
#         points = 32;
#     case _:
#         points = 60;

# using if statements
if books_bought < 1:
    points = 0
elif books_bought == 1:
    points = 6
elif books_bought == 2:
    points = 16
elif books_bought == 3:
    points = 32
else:
    points = 64

print("You bought:", books_bought, "books, earning", points, "points.")