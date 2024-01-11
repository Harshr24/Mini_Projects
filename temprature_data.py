from tabulate import tabulate  # Import the 'tabulate' library for creating tables
import random

# Generate alternate random temperatures for each day at different hours rounded to 2 decimal places 
# Nested list comprehension to create a list of lists (31 days x 24 hours) of random temperatures
temps = [[round(random.uniform(-10, 40), 2) if h % 2 == 0 else round(random.uniform(-5, 35), 2) for h in range(24)]  for d in range(31)] 

    # Explanation of the 'temps' generation:
    # - 'temps' is a list containing 31 sublists (representing 31 days)
    # - Each sublist contains 24 temperatures, alternating between two ranges:
    #   - Even-indexed hours (0, 2, 4, ...) have temperatures between -10 and 40 degrees Celsius
    #   - Odd-indexed hours (1, 3, 5, ...) have temperatures between -5 and 35 degrees Celsius

table_headers = [f"{i+1}" for i in range(24)]                           # Create headers for the table, representing each hour from 1 to 24
table_rows = [[f"Day {i + 1}"] + [f"{temp:.2f}" for temp in day_temps]  # Constructing rows for each day with temperatures rounded to 2 decimal places
    for i, day_temps in enumerate(temps)                                # Enumerate through 'temps' to get day numbers and temperatures for each day
]

table = tabulate(table_rows, headers=table_headers, tablefmt="pretty")
print(table)

# Function to calculate average temperature at a specific hour
def calculate_average_temperature_at_hour(temps, hour):
    total = sum(day[hour] for day in temps)
    return round(total / len(temps), 2)

# Function to count cool days (temperature at midnight <= 0 ℃)
def count_cool_days(temps):
    cool_days = sum(1 for day in temps if day[0] <= 0.0)
    return cool_days

# Function to find the hottest day and its temperature
def find_hottest_day(temps):
    max_temp = max(max(day) for day in temps)
    hottest_day = [i for i, day in enumerate(temps) if max_temp in day]
    return hottest_day[0], max_temp

# Function to find the coolest day and its temperature
def find_coolest_day(temps):
    min_temp = min(min(day) for day in temps)
    coolest_day = [i for i, day in enumerate(temps) if min_temp in day]
    return coolest_day[0], min_temp

# Function to count hot days (temperature at noon >= 20 ℃)
def count_hot_days(temps):
    hot_days = sum(1 for day in temps if day[11] >= 20.0)
    return hot_days

# User choice for operation
while True:
    user_choice = 0
    while user_choice < 1 or user_choice > 5:
        user_choice = int(input("Enter the operation to perform:\n1. Average temperature at noon\n2. Number of considerable cool days\n3. Number of hot days\n4. Hottest day and its temperature\n5. Coolest day and its temperature\nEnter your choice (1-5): "))
        if user_choice < 1 or user_choice > 5:
            print("Invalid choice! Please enter a number between 1 and 5.")

    if user_choice == 1:
        average_noon_temp = calculate_average_temperature_at_hour(temps, 11)
        print("Average temperature at noon:", average_noon_temp)
    elif user_choice == 2:
        cool_days_count = count_cool_days(temps)
        print(f"There were {cool_days_count} days with a temperature of 0°C or lower at midnight.")
    elif user_choice == 3:
        hot_days_count = count_hot_days(temps)
        print(f"There were {hot_days_count} days with a temperature of 20°C or higher at noon.")
    elif user_choice == 4:
        hottest_day_index, hottest_temp = find_hottest_day(temps)
        print(f"The hottest day was Day {hottest_day_index + 1} with a temperature of {hottest_temp}°C.")
    elif user_choice == 5:
        coolest_day_index, coolest_temp = find_coolest_day(temps)
        print(f"The coolest day was Day {coolest_day_index + 1} with a temperature of {coolest_temp}°C.")
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

    repeat = input("Do you want to perform another operation? (yes/no): ")
    if repeat.lower() != "yes":
        break