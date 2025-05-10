# midterm review - assignments 2 - primary colors mixers

P_COLORS = ["red", "yellow", "blue"]

color1 = input("Please enter a color name: ")
while True:
    if color1 in P_COLORS:
        break
    else:
        color1 = input("Enter valid primary color name for your first color: ")


color2 = input("enter primary color 2")
while True:
    if color2 in P_COLORS:
        break
    else:
        color2 = input("Enter valid secondary color name for your second color: ")
color_mix = "default color"

if color1 != color2:
    if color1 == P_COLORS[0] and color2 == P_COLORS[1]:
        color_mix = "orange"
    elif color1 == P_COLORS[0] and color2 == P_COLORS[2]:
        color_mix = "purple"
    elif color1 == P_COLORS[1] and color2 == P_COLORS[0]:
        color_mix = "orange"
    elif color1 == P_COLORS[1] and color2 == P_COLORS[2]:
        color_mix = "green"
    elif color1 == P_COLORS[2] and color2 == P_COLORS[0]:
        color_mix = "purple"
    elif color1 == P_COLORS[2] and color2 == P_COLORS[1]:
        color_mix = "green"
else:
    color_mix = color1 # no mixing colors were the same

print(color_mix)

