print("Please enter a character: ")
MY_CHAR = input()[0]

ASCII_VALUE_MY_CHAR = ord(MY_CHAR)

ASCII_A = 65
ASCII_Z = 90
ASCII_a = 97
ASCII_z = 122
ASCII_0 = 48
ASCII_9 = 57

if (ASCII_VALUE_MY_CHAR>=ASCII_A and ASCII_VALUE_MY_CHAR<=ASCII_Z) or (ASCII_VALUE_MY_CHAR>=ASCII_a and ASCII_VALUE_MY_CHAR<=ASCII_z):
    print(f"Character: {MY_CHAR} is an alphabet!")
elif ASCII_VALUE_MY_CHAR>=ASCII_0 and ASCII_VALUE_MY_CHAR<=ASCII_9:
    print(f"Character: {MY_CHAR} is a digit!")
else:
    print(f"Character: {MY_CHAR} is a special character!")