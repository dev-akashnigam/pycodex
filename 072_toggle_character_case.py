print("Please enter a character: ")
MY_CHAR = input()[0]

if MY_CHAR.isupper():
    TOGGLED_CASE_CHAR = MY_CHAR.lower()
else:
    TOGGLED_CASE_CHAR = MY_CHAR.upper()

print(f"Character: {MY_CHAR} on case toggling becomes = {TOGGLED_CASE_CHAR}")