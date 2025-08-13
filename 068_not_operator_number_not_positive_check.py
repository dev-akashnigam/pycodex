print("Please enter a positive or negative number: ")
MY_NUM = int(input())

if not MY_NUM>=0:
    print(f"{MY_NUM} is negative!")
else:
    print(f"{MY_NUM} is positive!")