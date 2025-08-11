print("Please enter a character: ")
MY_CHAR = input()[0]

if MY_CHAR.isalpha():
    print(f"Character: {MY_CHAR} is an alphabet!")
elif MY_CHAR.isdigit():
    print(f"Character: {MY_CHAR} is a digit!")
else:
    print(f"Character: {MY_CHAR} is a special character!")