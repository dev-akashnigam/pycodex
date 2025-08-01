import math

print("Please enter a number for which logarithms needs to be calculated : ")
NUMBER = float(input())

NATURAL_LOG = math.log(NUMBER)
COMMON_LOG = math.log10(NUMBER)
BINARY_LOG = math.log2(NUMBER)

print(f"Natural Log (log base e) of number:{NUMBER} = {NATURAL_LOG}")
print(f"Common Log (log base 10) of number:{NUMBER} = {COMMON_LOG}")
print(f"Binary Log (log base 2) of number:{NUMBER} = {BINARY_LOG}")