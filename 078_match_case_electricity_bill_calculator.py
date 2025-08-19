print("Please enter number of units consumed: ")
MY_UNITS_CONSUMED = int(input())

RATE_PER_UNIT_1ST_100_UNITS = 3.0
RATE_PER_UNIT_2ND_100_UNITS = 4.5
RATE_PER_UNIT_3RD_100_UNITS = 6.0
RATE_PER_UNIT_4TH_100_UNITS = 7.5

match MY_UNITS_CONSUMED:
    case units if units<=100:
        total_bill = (MY_UNITS_CONSUMED * RATE_PER_UNIT_1ST_100_UNITS)
    case units if units<=200:
        total_bill = (100 * RATE_PER_UNIT_1ST_100_UNITS) + ((MY_UNITS_CONSUMED - 100) * RATE_PER_UNIT_2ND_100_UNITS)
    case units if units<=300:
        total_bill = (100 * RATE_PER_UNIT_1ST_100_UNITS) + (100 * RATE_PER_UNIT_2ND_100_UNITS) + ((MY_UNITS_CONSUMED - 200) * RATE_PER_UNIT_3RD_100_UNITS)
    case _:
        total_bill = (100 * RATE_PER_UNIT_1ST_100_UNITS) + (100 * RATE_PER_UNIT_2ND_100_UNITS) + (100 * RATE_PER_UNIT_3RD_100_UNITS) + ((MY_UNITS_CONSUMED - 300) * RATE_PER_UNIT_4TH_100_UNITS)

print(f"Total Bill: {total_bill}")