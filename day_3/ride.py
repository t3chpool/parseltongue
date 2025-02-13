print("Welcome to the Rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Your ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket is $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!.")
    else:
        bill = 12
        print("Your ticket is $12.")
        
    wants_photo = input("Do you want your photo on the ride? Reply with Y or N: ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")
