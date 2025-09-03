def print_table(num):
    for i in range(1, 11, 1):
        print(f"{num} X {i} = {num*i}")

print("Please enter a number: ")
my_num = int(input())

print_table(my_num)