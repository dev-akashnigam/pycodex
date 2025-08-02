import math

print("Please enter a decimal number : ")
DECIMAL_NO = float(input())

print("Please enter the number of decimal places till which the decimal number should be rounded, truncated and formatted")
N = int(input())

ROUNDED_DECIMAL_NO = round(DECIMAL_NO, N)
TRUNCATED_DECIMAL_NO = math.trunc( DECIMAL_NO * (10 ** N) ) / (10 ** N)
FORMATTED_DECIMAL_NO = f"{DECIMAL_NO:.{N}f}"

print(f"Rounding decimal number {DECIMAL_NO} to {N} decimal places, the number becomes = {ROUNDED_DECIMAL_NO}")
print(f"Truncating decimal number {DECIMAL_NO} to {N} decimal places, the number becomes = {TRUNCATED_DECIMAL_NO}")
print(f"Formatting decimal number {DECIMAL_NO} to {N} decimal places, the number becomes = {FORMATTED_DECIMAL_NO}")

"""
Please enter a decimal number : 
9865.15648513
Please enter the number of decimal places till which the decimal number should be rounded, truncated and formatted
4
Rounding decimal number 9865.15648513 to 4 decimal places, the number becomes = 9865.1565
Truncating decimal number 9865.15648513 to 4 decimal places, the number becomes = 9865.1564
Formatting decimal number 9865.15648513 to 4 decimal places, the number becomes = 9865.1565
"""