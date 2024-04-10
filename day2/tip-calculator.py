print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What tip would you like to give? 10, 12 or 15? ")) / 100
people = int(input("How many people to split? "))

payment = (bill + bill * tip) / people
payment_format = "{:.2f}".format(payment)
print(f"Each person should pay: ${payment_format}")

