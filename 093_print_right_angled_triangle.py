print("Please enter the number of rows to print in the right angled triangle:")
myRows = int(input())

for i in range(1, myRows+1, 1):
    for j in range(1, i+1, 1):
        print("*", end=" ")
    print()

