print("Please enter day number (1-7): ")
MY_DAY_NO = int(input())

match MY_DAY_NO:
    case 1:
        dayName = "MONDAY"
    case 2:
        dayName = "TUESDAY"
    case 3:
        dayName = "WEDNESDAY"
    case 4:
        dayName = "THURSDAY"
    case 5:
        dayName = "FRIDAY"
    case 6:
        dayName = "SATURDAY"
    case 7:
        dayName = "SUNDAY"
    case _:
        dayName = "UNDEFINED"

print(f"Day {MY_DAY_NO} represents = {dayName}")