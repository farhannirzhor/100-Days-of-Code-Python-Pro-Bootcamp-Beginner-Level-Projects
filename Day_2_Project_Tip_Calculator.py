print("Welcome to the tip calculator!")
t_bill = float(input("What was the total bill? $"))
g_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
payable_amount = (((g_tip / 100) * t_bill) + t_bill) / split
final_amount = round(payable_amount, 2)
print(f"Each person should pay: ${final_amount}")