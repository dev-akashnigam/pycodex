print("Please enter the number of terms to print in the fibonacci series: ")
totalNoOfTermsToPrint = int(input())

firstTerm = 0
secondTerm = 1

if totalNoOfTermsToPrint==0:
    print()
elif totalNoOfTermsToPrint==1:
    print(firstTerm)
elif totalNoOfTermsToPrint==2:
    print(f"{firstTerm} {secondTerm} ")
else:
    print(f"{firstTerm} {secondTerm}", end=" ")
    currentCountOfTermsPrinted = 2
    while currentCountOfTermsPrinted < totalNoOfTermsToPrint:
        nextTerm = firstTerm + secondTerm
        print(f"{nextTerm}", end=" ")

        firstTerm = secondTerm
        secondTerm = nextTerm
        currentCountOfTermsPrinted += 1

