print("Please enter the first number: ")
my_first_number = int(input())

print("Please enter the second number: ")
my_second_number = int(input())

smaller_number = min(my_first_number, my_second_number)
greater_number = max(my_first_number, my_second_number)

hcf = 1
if greater_number%smaller_number==0:
    hcf = smaller_number
else:
    half_of_smaller_number = int(smaller_number/2)
    for i in range (half_of_smaller_number, 1, -1):
        if greater_number%i==0 and smaller_number%i==0:
            hcf = i
            break
print(f"HCF of {my_first_number} and {my_second_number} = {hcf}")


