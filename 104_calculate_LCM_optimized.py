print("Please enter the first number: ")
my_first_number = int(input())
original_first_num = my_first_number

print("Please enter the second number: ")
my_second_number = int(input())
original_second_number = my_second_number

while (my_second_number!=0):
    mod = my_first_number % my_second_number
    my_first_number = my_second_number
    my_second_number = mod

hcf = my_first_number

lcm = (original_first_num/hcf) * original_second_number

print(f"LCM = {lcm}")

