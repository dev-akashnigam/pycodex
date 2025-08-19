print("Please enter marks (0-100): ")
MY_MARKS = int(input())

match MY_MARKS:
    case mark if (mark>=90 and mark<=100):
        grade = 'A'
    case mark if (mark>=80 and mark<=89):
        grade = 'B'
    case mark if (mark>=70 and mark<=79):
        grade = 'C'
    case mark if (mark>=60 and mark<=69):
        grade = 'D'
    case _:
        grade = 'E'

print(f"Marks: {MY_MARKS} correspond to grade = {grade}")
    