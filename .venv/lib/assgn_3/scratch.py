questions_incorrect = []
score = 0
student_exam = open('student_answers.txt', "r")
student_answers = []
for line in student_exam:
    value = line.split('"')[1]
    student_answers.append(value)

print(student_answers)
