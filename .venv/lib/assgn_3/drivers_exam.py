# midterm review - assignment 3 - drivers license exam

ANSWER_KEY = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A", ]
PASSING_SCORE = 15
QUESTIONS = 20

questions_incorrect = []
score = 0
student_exam = open('student_answers.txt', "r")
student_answers = []
for line in student_exam:
    value = line.split('"')[1]
    student_answers.append(value)

print(student_answers)
print(len(student_answers))

i = 0
while i < len(ANSWER_KEY):
    if ANSWER_KEY[i] in student_answers[i]:
        score+=1
    else:
        questions_incorrect.append(i + 1)
    i += 1

print("score is", score)
if score >= PASSING_SCORE:
    print("PASS")

print("questions incorrect: ", questions_incorrect)