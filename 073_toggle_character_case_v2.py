print("Please enter a character: ")
MY_CHAR = input()[0]

ASCII_MY_CHAR = ord(MY_CHAR)

if 65<=ASCII_MY_CHAR<=90:
    TOGGLED_CHAR = chr(ASCII_MY_CHAR + 32)
else:
    TOGGLED_CHAR = chr(ASCII_MY_CHAR - 32)

print(f"Character: {MY_CHAR} on case toggling becomes = {TOGGLED_CHAR}")