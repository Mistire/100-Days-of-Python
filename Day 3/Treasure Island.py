print("Welcome to Tresure Island")
print("Your mission is to find the treasure")

cross_road = input("You are at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
if cross_road == "Left":
  lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n")
  if lake == "wait":
    doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
    if doors == "blue":
      print("You enter a room full of Beasts and got eaten. Game Over!")
    elif doors == "yellow":
      print("You enter a room full with treasures. You win!!!")
    elif doors == "Red":
      print("You enter a room that is on fire and got burned by the fire. Game Over!")
    else:
      print("Game Over!")
  else:
    print("You stat swimming and suddenly you got attacked by a trout. Game Over!")
else:
  print("You fall into a hole. Game Over!")