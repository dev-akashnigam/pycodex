print("Please enter a year: ")
MY_YEAR = int(input())

IS_LEAP_YEAR = (True if MY_YEAR%400 == 0 else False) if MY_YEAR%100 == 0 else (True if MY_YEAR%4 == 0 else False)

print(f"Year: {MY_YEAR} is a leap year = {IS_LEAP_YEAR}")