print("Please enter the natural number till where you need the sum: ")
myNaturalNo = int(input())

sum = 0

for i in range(1, myNaturalNo+1, 1):
    sum += i

print(f"Sum of first {myNaturalNo} natural numbers = {sum}")