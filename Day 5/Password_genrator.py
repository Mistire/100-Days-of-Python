import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPasword generator\n")

letter_amount = int(input("How many letter would you want in your password:\n "))
number_amount = int(input("How many numbers do want in your password:\n "))
symbol_amount = int(input("How many symbols do you want in your password:\n "))

pass_list = []

for _ in range(letter_amount):
  pass_list.append(random.choice(letters))

for _ in range(number_amount):
  pass_list.append(random.choice(numbers))

for _ in range(symbol_amount):
  pass_list.append(random.choice(symbols))

random.shuffle(pass_list)
pass_str = "".join(pass_list)

print("\nYour generated password is: ", pass_str, "\n")
