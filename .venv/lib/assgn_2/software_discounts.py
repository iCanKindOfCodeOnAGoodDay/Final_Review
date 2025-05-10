# midterm review - assignment 2 - Software Discounts

packagesCount = 0.0
while True:
    try:
        packagesCount = float(input("How many packages would you like to buy?"))
        if packagesCount > 0:
            break
        else:
            raise Exception(e)
    except:
        print("Please enter a valid number.")
discountPercent = 0.00
retailPrice = 99
if packagesCount < 10:
    print('no discount')
elif packagesCount < 20:
    discountPercent = 0.20
elif packagesCount < 50:
    discountPercent = 0.30
elif packagesCount < 100:
    discountPercent = 0.40
else:
    discountPercent = 0.50
subtotal = retailPrice * packagesCount
total = subtotal * discountPercent
print("you purchased", packagesCount, "packages, earning", discountPercent, "% discount, your subtotal before discount was $", subtotal, "and your total after discount is $", total )