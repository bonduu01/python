#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bid_choice = "yes"
highest_bid = 0
name = ''
bid_winner = {}
while bid_choice == "yes":
  #data_dictionary{}
  input_name = input("What is your name?: ")
  input_bid = int(input("What's your bid?: $"))
  
  if input_bid > highest_bid:
      bid_winner["name"] = input_name
      bid_winner["bid"] = input_bid
      highest_bid = input_bid
      name = input_name
  
  bid_choice = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  
print (f"The winner is {name} with a bid of ${highest_bid}")

