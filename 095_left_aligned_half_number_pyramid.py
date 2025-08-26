print("Please enter the number of rows to be printed in the left aligned half number pyramid: ")
my_rows = int(input())

for i in range(1, my_rows+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()