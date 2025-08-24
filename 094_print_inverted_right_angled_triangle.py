print("Please enter the number of rows to be printed in the inverted right angled triangle: ")
my_rows = int(input())

for i in range(my_rows, 0, -1):
    for j in range(1, i+1, 1):
        print("*", end=" ")
    print()