print("Please enter a number: ")
my_num = int(input())

sum_of_digits = 0
while my_num!=0:
    last_digit = my_num % 10
    sum_of_digits += last_digit
    my_num = my_num // 10

print(f"Sum of digits = {sum_of_digits}")