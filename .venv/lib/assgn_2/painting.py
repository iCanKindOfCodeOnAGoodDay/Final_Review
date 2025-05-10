# midterm review - Assignment 2 - house painter - cost estimation

LABOR_RATE = 22
GALLON_COVERAGE = 116
GALLON_TIME = 8

wall_space = float(input("what's the wall space? "))
gallon_cost = float(input("what's the gallon cost? "))

paint_cost_square_foot = gallon_cost / GALLON_COVERAGE
total_paint_cost = wall_space * paint_cost_square_foot

# each 116 square feet takes 8 hours of labor
labor_needed = wall_space / GALLON_COVERAGE * GALLON_TIME
total_labor_cost = labor_needed * LABOR_RATE

total_cost = total_paint_cost + total_labor_cost

print("total paint cost: ", total_cost)
print("total labor cost: ", total_labor_cost)
print("total paint cost: ", total_paint_cost)
