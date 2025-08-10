print("Please enter a year : ")
MY_YEAR = int(input())

if MY_YEAR%100 == 0 : 
    if MY_YEAR%400 == 0 : 
        print(f"Year: {MY_YEAR} is a leap year!")
    else :
        print(f"Year: {MY_YEAR} is NOT a leap year!")
else :
    if MY_YEAR%4 == 0 :
        print(f"Year: {MY_YEAR} is a leap year!")
    else :
        print(f"Year: {MY_YEAR} is NOT a leap year!")