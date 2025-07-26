import sys

allCommandLineArgumentsList = sys.argv # sys.argv returns a LIST of command line args as strings.

countOfCommandLineArgs = len(allCommandLineArgumentsList)

print(f"Total number of command line arguments : {countOfCommandLineArgs}")

defaultCommandLineArgument = allCommandLineArgumentsList[0]  # First command line argument in PY is always default argument
print(f"PYTH Provided Command Line Argument 0 : {defaultCommandLineArgument}")

if countOfCommandLineArgs > 1:
    userProvidedCommandLineArgumentsList = allCommandLineArgumentsList[1:]
    index = 1
    for item in userProvidedCommandLineArgumentsList:
        print(f"USER Provided Command Line Argument {index} : {item}")
        index += 1
else:
    print("There are no user provided command line arguments passed at the time of running the code")