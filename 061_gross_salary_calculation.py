"""
Objective:
Write a program that takes marks for five subjects, computes the total and percentage, and assigns a grade based on a defined percentage–grade 
mapping using an if-else ladder.

Input:
Prompt the user to enter marks obtained in five different subjects (e.g., Math, English, Science, Social Studies, Computer).
You may assume each subject is out of 100 marks.
Data type can be int or float depending on whether marks can have decimals.

Grade Assignment:
90% and above:	A
80% to <90%  :	B
70% to <80%  :	C
60% to <70%	 :  D
40% to <60%	 :  E
Below 40%	 :  F
"""

print("Please enter basic salary: ")
MY_BASIC_SALARY = float(input())

if MY_BASIC_SALARY<=10000:
    hra_percentage = 20
    da_percentage = 80
elif MY_BASIC_SALARY>10000 and MY_BASIC_SALARY<20000:
    hra_percentage = 25
    da_percentage = 90
else:
    hra_percentage = 30
    da_percentage = 95

hra_amount = MY_BASIC_SALARY * (hra_percentage/100.0)
da_amount = MY_BASIC_SALARY * (da_percentage/100.0)

GROSS_SALARY = MY_BASIC_SALARY + hra_amount + da_amount

print(f"Basic Salary: {MY_BASIC_SALARY}")
print(f"HRA ({hra_percentage}%): {hra_amount}")
print(f"HRA ({da_percentage}%): {da_amount}")
print(f"Gross Salary: {GROSS_SALARY}")








