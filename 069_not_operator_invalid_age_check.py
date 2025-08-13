print("Please enter your age: ")
MY_AGE = int(input())

if not (MY_AGE>0 and MY_AGE<=120):
    print(f"Age: {MY_AGE} is invalid!")
else:
    print(f"Age: {MY_AGE} is valid!")