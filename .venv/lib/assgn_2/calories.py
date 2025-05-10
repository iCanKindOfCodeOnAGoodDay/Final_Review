# midterm review - assignment 2 - calories from fat and carbs

fatGrams = 0.0

while True:
    try:
        fatGrams = float(input('enter fat grams: '))
        if fatGrams > 0:
            break
        else:
            raise Exception(e)
    except Exception:
        print('enter number above zero')


carbGrams = 0.0

while True:
    try:
        carbGrams = float(input('enter carb grams: '))
        if carbGrams > 0:
            break
        else:
            raise Exception(e)
    except:
        print('enter number above zero')

# fat cals = grams * 8
# carb cals = grams * 3

fatCals = fatGrams * 8
carbCals = carbGrams * 3

print("fat calories are", fatCals, "and carb calories are", carbCals, "and total calories are", fatCals + carbCals)