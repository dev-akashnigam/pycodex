import math

print("Please enter a number: ")
myNum = int(input())

noOfDigits = 0
while myNum!= 0:
    noOfDigits += 1
    myNum = myNum // 10

print(f"Number of digits = {noOfDigits}")