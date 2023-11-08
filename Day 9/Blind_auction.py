import os
from art import logo


print(logo)
more_biders = True
bid = {}

def highest_bid(bid_d):
  highest_bid = 0
  winner = ""
  for bidder_name in bid_d:
    bid_amount = bid_d[bidder_name]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder_name
  print(f"The Winner is {winner} with ${highest_bid}")

while more_biders:
  bidder_name = input("Enter your name: ")
  bid_amount = int(input("Enter your bid: $"))
  bid[bidder_name] = bid_amount
  
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if other_bidder == "no":
    more_biders = False
    highest_bid(bid_d=bid)
  elif other_bidder == "yes":
    os.system('cls')

