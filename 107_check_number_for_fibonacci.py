import math
print("Please enter the number to determine if its part of the fibonacci sequence or not")
my_num = int(input())

five_N_square = 5 * my_num * my_num
five_N_square_plus_4 = five_N_square + 4
five_N_square_minus_4 = five_N_square - 4

integer_square_root_of_five_N_square_plus_4 = math.isqrt(five_N_square_plus_4)
integer_square_root_of_five_N_square_minus_4 = math.isqrt(five_N_square_minus_4)

is_five_N_square_plus_4_perfect_square = integer_square_root_of_five_N_square_plus_4 * integer_square_root_of_five_N_square_plus_4 == five_N_square_plus_4
is_five_N_square_minus_4_perfect_square = integer_square_root_of_five_N_square_minus_4 * integer_square_root_of_five_N_square_minus_4 == five_N_square_minus_4

if is_five_N_square_plus_4_perfect_square or is_five_N_square_minus_4_perfect_square:
    print(f"{my_num} is a fibonacci number.")
else:
    print(f"{my_num} is a NOT a fibonacci number.")