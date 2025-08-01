import math

print("Please enter initial amount : ")
principal = float(input())

print("Please enter rate of interest (in decimals not percentage) : ")
rate = float(input())

print("Please enter time in years : ")
time = float(input())

finalAmount = principal * math.pow(math.e, rate*time)
print(f"Final amount received on investment of amount:{principal} for {time} years at {rate} rate of interest = {finalAmount}")