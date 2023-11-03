print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

final_bill = (total_bill + ((tip_percentage / 100) * total_bill)) / people

print(f"Each person should pay: ${final_bill:.1F}")