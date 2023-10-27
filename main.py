# Import Modules
import random

# Create lists of possible password Characters
letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# Welcome Message
print("Welcome to the PyPassword generator!")
print("Please enter your desired amount of letters, numbers, and symbols for your password.\n")

# User Inputs
num_letters = int(input("How many letters: "))
num_numbers = int(input("How many numbers: "))
num_symbols = int(input("How many symbols: "))

# Selecting random digits
unmixed_password = []

for i in range(0, num_letters):
    unmixed_password += random.choice(letters_list)
for i in range(0, num_numbers):
    unmixed_password += random.choice(numbers_list)
for i in range(0, num_symbols):
    unmixed_password += random.choice(symbols_list)

# Mixing digits to create password
final_password = ""

for i in range(0, len(unmixed_password)):
    final_password += (unmixed_password.pop(unmixed_password.index(random.choice(unmixed_password))))

# Display final password
print(f"\nYour password is: {final_password}")




