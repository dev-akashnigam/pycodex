print("Please enter the first number: ")
first_num = int(input())

print("Please enter the second number: ")
second_num = int(input())

while second_num!=0:
    mod = first_num % second_num
    first_num = second_num
    second_num = mod

print(f"HCF = {first_num}")