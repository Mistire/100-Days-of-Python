from hangman_word_list import word_list
from hangman_art import logo, stages
import random

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print("pssst:", chosen_word)

display = []
for _ in range(len(chosen_word)):
  display.append("_")

print(logo)
while not end_of_game:

  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(word_length):
    letter = chosen_word[position] 
    if letter == guess:
      display[position] = guess
  if guess not in chosen_word: 
    lives -= 1

    if lives == 0:
      end_of_game = True
      print("You lose")
  print(f"{' '.join(display)}")
  if "_" not in display:
    end_of_game = True
    print("You have won")
  print(stages[lives]) 