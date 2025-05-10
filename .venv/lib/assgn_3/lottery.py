# midterm review - lottery number generator - assignment 3
import random
lotteryNumbers = [random.randint(0, 99) for i in range(9)]
print(", ".join(str(num) for num in lotteryNumbers))
# win = ''
# for lotteryNumber in lotteryNumbers:
#     win += str(lotteryNumber) + ","
# win = win.rstrip(",")
# if win.endswith(","):
#     win = win[:-1]
#print(win)
