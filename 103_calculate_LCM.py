print("Please enter the first number: ")
my_first_number = int(input())

print("Please enter the second number: ")
my_second_number = int(input())

greater_number = max(my_first_number, my_second_number)
smaller_number = min(my_first_number, my_second_number)

lcm = my_first_number * my_second_number
if greater_number%smaller_number == 0:
    lcm = greater_number
else:
    multiple = 2
    while (greater_number*multiple)%smaller_number!=0:
        multiple += 1
    lcm = greater_number*multiple
print(f"LCM of {my_first_number} and {my_second_number} = {lcm}")


