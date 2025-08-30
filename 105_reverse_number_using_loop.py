print("Please enter the number to be reversed: ")
my_num = int(input())

original_number = my_num
reversed_num = 0

while my_num!=0:
    last_digit = my_num % 10
    reversed_num = (reversed_num * 10) + last_digit

    my_num //= 10

print(f"Reverse of number: {original_number} = {reversed_num}")