print("Please enter the number for which factorial has to be calculated: ")
MY_NUM = int(input())

factorial = 1
for i in range(MY_NUM, 0, -1):
    factorial *= i

print(f"Factorial of {MY_NUM} = {factorial}")