import math

print("Please enter a number: ")
my_num = int(input())

while my_num!=0:
    last_digit = my_num % 10
    my_num = math.floor(my_num / 10)

    print(last_digit)