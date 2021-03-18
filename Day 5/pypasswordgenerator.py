import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]

sybmols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters you would you like in your password?\n"))
nr_symbols = int(input("How many Sybmols you would you like in your password?\n"))
nr_numbers = int(input("How many Numbers you would you like in your password?\n"))

# Easy Level

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(sybmols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = " "
for char in password_list:
    password += char

print(f"your password is{password}")

# Hard Level
