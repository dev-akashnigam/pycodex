print("Please enter the units of electricity consumed: ")
my_units_consumed = float(input())

COST_PER_UNIT_FOR_1ST_100_UNITS = 1.50
COST_PER_UNIT_FOR_2ND_100_UNITS = 2.00
COST_PER_UNIT_FOR_3RD_100_UNITS = 3.00
COST_PER_UNIT_FOR_300_ONWARDS_UNITS = 5.00

cost_of_consumption_for_1st_100_units = 0.0
cost_of_consumption_for_2nd_100_units = 0.0
cost_of_consumption_for_3rd_100_units = 0.0
cost_of_consumption_for_300_onwards_units = 0.0

if my_units_consumed<=100:
    cost_of_consumption_for_1st_100_units = my_units_consumed * COST_PER_UNIT_FOR_1ST_100_UNITS
elif my_units_consumed<=200:
    cost_of_consumption_for_1st_100_units = 100 * COST_PER_UNIT_FOR_1ST_100_UNITS
    cost_of_consumption_for_2nd_100_units = (my_units_consumed - 100) * COST_PER_UNIT_FOR_2ND_100_UNITS
elif my_units_consumed<=300:
    cost_of_consumption_for_1st_100_units = 100 * COST_PER_UNIT_FOR_1ST_100_UNITS
    cost_of_consumption_for_2nd_100_units = 100 * COST_PER_UNIT_FOR_2ND_100_UNITS
    cost_of_consumption_for_3rd_100_units = (my_units_consumed - 200) * COST_PER_UNIT_FOR_3RD_100_UNITS
else:
    cost_of_consumption_for_1st_100_units = 100 * COST_PER_UNIT_FOR_1ST_100_UNITS
    cost_of_consumption_for_2nd_100_units = 100 * COST_PER_UNIT_FOR_2ND_100_UNITS
    cost_of_consumption_for_3rd_100_units = 100 * COST_PER_UNIT_FOR_3RD_100_UNITS
    cost_of_consumption_for_300_onwards_units = (my_units_consumed - 300) * COST_PER_UNIT_FOR_300_ONWARDS_UNITS

TOTAL_COST_OF_ELECTRICITY_CONSUMPTION = cost_of_consumption_for_1st_100_units + cost_of_consumption_for_2nd_100_units + cost_of_consumption_for_3rd_100_units + cost_of_consumption_for_300_onwards_units

print(f"Total Bill: {TOTAL_COST_OF_ELECTRICITY_CONSUMPTION}")