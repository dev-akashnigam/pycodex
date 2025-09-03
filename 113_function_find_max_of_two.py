def getMaxOfTwo(a, b):
    if a>=b:
        return a
    else:
        return b
    
print("Please enter the first number: ")
first_num = int(input())

print("Please enter the second number: ")
second_num = int(input())

larger_num = getMaxOfTwo(first_num, second_num)

print(f"Larger amongst {first_num} and {second_num} = {larger_num}")