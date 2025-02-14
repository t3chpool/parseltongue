import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to Password Generator")
nr_letters = int(input("How many Letters ?\n"))
nr_symbols = int(input("How many Symbols ?\n"))
nr_numbers = int(input("How many characters ?\n"))


easy_password = ""

for x in range (0, nr_letters):
    easy_password += random.choice(letters)

for x in range (0, nr_numbers):
    easy_password += random.choice(numbers)

for x in range (0, nr_symbols):
    easy_password += random.choice(symbols)

print(f"This is your easy password: {easy_password}")


hard_password = []

for x in range (0, nr_letters):
    hard_password.append(random.choice(letters))
    
for x in range (0, nr_numbers):
    hard_password.append(random.choice(numbers))

for x in range (0, nr_symbols):
    hard_password.append(random.choice(symbols))
    
random.shuffle(hard_password) # shuffles items in the list

hard_password = "".join(hard_password) # converts list into string

print(f"This is your hard password: {hard_password}")
