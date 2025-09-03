print_table = lambda num : run(num)

def run(a):
    for i in range(1, 11, 1):
        print(f"{a} X {i} = {a*i}")

print("Please enter a number: ")
my_num = int(input())

print_table(my_num)