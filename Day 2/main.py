print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(
    input("What percantage tip would you like to give? 10, 12 or  15?"))
total_people = int(input("How many people to split the bill?"))

final_amount = total_bill * (1 + tip / 100) / total_people

output = f"Each person should pay: ${final_amount:.2f}"
print(output.format(final_amount))
