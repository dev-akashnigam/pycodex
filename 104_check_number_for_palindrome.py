print("Please enter a number: ")
my_number = int(input())

reversed_number = 0
original_number = my_number

while(my_number!=0):
    last_digit = my_number % 10
    reversed_number = (reversed_number * 10) + last_digit

    my_number //= 10
if reversed_number==original_number:
    print(f"Number: {original_number} is palindrome = true")
else:
    print(f"Number: {original_number} is palindrome = false")