import math

print("Please enter a number: ")
my_num = int(input())

if my_num<=1:
    isPrime = False
elif my_num==2 or my_num==3:
    isPrime = True
elif my_num%2==0:
    isPrime=False
else:
    isPrime = True
    for i in range(3, int(math.sqrt(my_num))+1, 2):
        if my_num%i==0:
            isPrime=False
            break

if isPrime:
    print(f"Number: {my_num} is prime.")
else:
    print(f"Number: {my_num} is not prime.")