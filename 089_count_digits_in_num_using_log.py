import math

print("Please enter a number: ")
myNum = int(input())

countOfDigits = math.floor(math.log10(myNum)) + 1

print(f"Number of digits = {countOfDigits}")