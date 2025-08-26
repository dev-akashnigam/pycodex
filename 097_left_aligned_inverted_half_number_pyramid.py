print("Please enter the number of rows to be printed in the inverted left aligned half number pyramid: ")
my_rows = int(input())

for i in range(1, my_rows+1, 1):
    for j in range(my_rows, i-1, -1):
        print(j, end=" ")
    print()