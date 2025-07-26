print("Please enter principal amount : ")
principal_amt = int(input())

print("Please enter rate of interest : ")
rate = float(input())

print("Please enter time period : ")
time_period = float(input())

simple_interest = (principal_amt * rate * time_period)/100

print(f"Simple interest earned on investment of amount {principal_amt} at {rate}% for {time_period} years is: {simple_interest}")



