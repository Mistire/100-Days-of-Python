from alphabet import alphabet
from art import logo

print(logo)
def caesar(plain_text, shift_amount, cipher_direction):
  ciphered_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = (position + shift_amount) % 26
      ciphered_text += alphabet[new_position]
    elif direction == "decode":
      new_position = (position - shift_amount) % 26
      ciphered_text += alphabet[new_position]
  print(f"The encoded text is: {ciphered_text}")

stop = False
while not stop:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

  repeat = input("Do you want to repeat? 'yes' or 'no'.\n")
  if repeat == "no":
    stop = True
    print("Good bye!!")
