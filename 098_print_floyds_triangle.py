print("Please enter the number of rows to be printed in Floyd's triange: ")
my_rows = int(input())

currentNumToPrint = 1
for i in range(1, my_rows+1, 1):
    for j in range(1, i+1, 1):
        print(currentNumToPrint, end=" ")
        currentNumToPrint += 1
    print()