import math

print("Please enter the number to be checked for perfect square: ")
my_num = int(input())

square_root_of_num = math.sqrt(my_num)

if square_root_of_num==math.floor(square_root_of_num):
    print(f"{my_num} is a perfect square.")
else:
    print(f"{my_num} is NOT a perfect square.")