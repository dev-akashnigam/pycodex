import math
print("Please enter a number: ")
my_num = int(input())

total_digits_in_num = int(math.floor(math.log10(my_num))) + 1

original_number = my_num
sum_of_last_digits_to_power_total_digits = 0

while my_num!=0:
    last_digit = my_num%10
    last_digit_to_power_total_digits = last_digit ** total_digits_in_num
    sum_of_last_digits_to_power_total_digits += last_digit_to_power_total_digits

    my_num //= 10

if sum_of_last_digits_to_power_total_digits==original_number:
    print(f"Number: {original_number} is an armstrong number.")
else:
    print(f"Number: {original_number} is NOT an armstrong number.")