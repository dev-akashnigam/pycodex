print("Please enter marks obtained in the first subject: ")
MARKS_SUBJECT_1 = float(input())

print("Please enter marks obtained in the second subject: ")
MARKS_SUBJECT_2 = float(input())

print("Please enter marks obtained in the third subject: ")
MARKS_SUBJECT_3 = float(input())

print("Please enter marks obtained in the fourth subject: ")
MARKS_SUBJECT_4 = float(input())

print("Please enter marks obtained in the fifth subject: ")
MARKS_SUBJECT_5 = float(input())

PERCENTAGE = ( (MARKS_SUBJECT_1 + MARKS_SUBJECT_2 + MARKS_SUBJECT_3 + MARKS_SUBJECT_4 + MARKS_SUBJECT_5 )/500) * 100

if PERCENTAGE>=90:
    grade = 'A'
elif PERCENTAGE>=80 and PERCENTAGE<90:
    grade = 'B'
elif PERCENTAGE>=70 and PERCENTAGE<80:
    grade = 'C'
elif PERCENTAGE>=60 and PERCENTAGE<70:
    grade = 'D'
elif PERCENTAGE>=40 and PERCENTAGE<60:
    grade = 'E'
else:
    grade = 'F'

print(f"Grade for percentage: {PERCENTAGE} = {grade}")