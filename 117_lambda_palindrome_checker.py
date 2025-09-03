is_palindrome = lambda num : if_palindrome(num)

def if_palindrome(num):
    original_number = num
    reversed_number = 0

    while num!=0:
        last_digit = num % 10
        reversed_number = (reversed_number * 10) + last_digit

        num //= 10
    
    return reversed_number == original_number

print("Please enter a number: ")
my_num = int(input())

is_num_palidrome = is_palindrome(my_num)

print(f"Number: {my_num} is palindrome = {is_num_palidrome}")