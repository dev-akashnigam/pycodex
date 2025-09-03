def get_square(num):
    square = num * num
    return square

print("Please enter an integer: ")
my_num = int(input())

square = get_square(my_num)

print(f"Square of number: {my_num} = {square}")
