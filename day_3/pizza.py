print("Wlecome to Python Pizza Devliery")
size = input("What size of Pizza you want? S, M or L: ")
pepperoni = input("Do you wnat pepperoni on you pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"your total bill is ${bill}. ")
