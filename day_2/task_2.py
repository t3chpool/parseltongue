# Data Types

print("Welcome to the tip calculator") 
total_bill = int(input("What was the total bill? $"))
tip = int(input("How much percent tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
amount_per_person = ((total_bill * (tip / 100)) + total_bill )/ number_of_people
print(f"Each person should pay: $ {round(amount_per_person, 2)}")
