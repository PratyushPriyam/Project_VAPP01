#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_string = ""

for l in range(0,nr_letters):
    randLetter = random.choice(letters)
    password_string += randLetter


for l in range(0,nr_symbols):
    randSymbol = random.choice(symbols)
    password_string += randSymbol


for l in range(0,nr_numbers):
    randNumber = random.choice(numbers)
    password_string += randNumber

password_list = list(password_string)
random.shuffle(password_list)

final_password = ""
for char in password_list:
    final_password += char
    list(final_password)
print("Final Password is :" + final_password)

