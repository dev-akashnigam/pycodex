print("Please enter principal amount : ")
principalAmt = int(input())

print("Please enter rate of interest : ")
rate = float(input())

print("Please enter time period : ")
timePeriod = float(input())

simpleInterest = (principalAmt * rate * timePeriod)/100

print(f"Simple interest earned on investment of amount {principalAmt} at {rate}% for {timePeriod} years is: {simpleInterest}")



