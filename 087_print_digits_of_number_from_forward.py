import math

print("Please enter a number: ")
my_num = int(input())

my_num_copy = my_num

count_of_digits = 0
while my_num!=0:
    count_of_digits += 1
    my_num = math.floor(my_num / 10)

my_num = my_num_copy

divisor = 10 ** (count_of_digits-1)

while divisor!=0:
    first_digit = math.floor(my_num / divisor)
    print(first_digit)

    my_num = my_num % divisor
    divisor = math.floor(divisor / 10)