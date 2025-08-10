print("Please enter a number: ")
MY_NUM = int(input())

if MY_NUM%5 == 0:
    if MY_NUM%11 == 0:
        print(f"Number: {MY_NUM} is divisible by both 5 and 11.")
    else:
        print(f"Number: {MY_NUM} is divisible by 5 but not by 11.")
else:
    if MY_NUM%11 == 0:
        print(f"Number: {MY_NUM} is not divisible by 5 but divisible by 11.")
    else:
        print(f"Number: {MY_NUM} is not divisible by both 5 and 11.")