import sys

all_command_line_arguments_list = sys.argv # sys.argv returns a LIST of command line args as strings.

count_of_command_line_args = len(all_command_line_arguments_list)

print(f"Total number of command line arguments : {count_of_command_line_args}")

default_command_line_argument = all_command_line_arguments_list[0]  # First command line argument in PY is always default argument
print(f"PYTH Provided Command Line Argument 0 : {default_command_line_argument}")

if count_of_command_line_args > 1:
    userProvidedCommandLineArgumentsList = all_command_line_arguments_list[1:]
    index = 1
    for item in userProvidedCommandLineArgumentsList:
        print(f"USER Provided Command Line Argument {index} : {item}")
        index += 1
else:
    print("There are no user provided command line arguments passed at the time of running the code")