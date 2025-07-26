print("Please enter a decimal number : ")
decimal_no = float(input())

rounded_to_nearest_integer = round(decimal_no)
rounded_to_first_decimal_place = round(decimal_no, 1)
rounded_to_second_decimal_place = round(decimal_no, 2)
rounded_to_third_decimal_place = round(decimal_no, 3)

print(f"{decimal_no} when rounded to nearest integer becomes : {rounded_to_nearest_integer}")
print(f"{decimal_no} when rounded to first decimal place becomes : {rounded_to_first_decimal_place}")
print(f"{decimal_no} when rounded to second decimal place becomes : {rounded_to_second_decimal_place}")
print(f"{decimal_no} when rounded to third decimal place becomes : {rounded_to_third_decimal_place}")