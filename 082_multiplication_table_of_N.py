print("Please enter the number for which you want multiplication table: ")
MY_NUM = int(input())

for i in range(1, 11, 1):
    print(f"{MY_NUM} X {i} = {MY_NUM * i}")