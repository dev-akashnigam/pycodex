import math

print("Please enter a decimal number to be truncated : ")
decimalNo = float(input())

truncated_to_0_decimal_place = math.trunc(decimalNo)
truncated_to_1_decimal_place = (math.trunc(decimalNo * 10))/10.0
truncated_to_2_decimal_place = (math.trunc(decimalNo * 100))/100.0
truncated_to_3_decimal_place = (math.trunc(decimalNo * 1000))/1000.0

print(f"Truncating {decimalNo} to 0 decimal place results in = {truncated_to_0_decimal_place}")
print(f"Truncating {decimalNo} to 1 decimal place results in = {truncated_to_1_decimal_place}")
print(f"Truncating {decimalNo} to 2 decimal place results in = {truncated_to_2_decimal_place}")
print(f"Truncating {decimalNo} to 3 decimal place results in = {truncated_to_3_decimal_place}")
                                