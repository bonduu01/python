from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
final_choice = True
data_dictionary = {}
bid_choice = "yes"
data_host = []
i = 0
while bid_choice == "yes":
  #data_dictionary{}
  input_name = input("What is your name?: ")
  input_bid = input("What's your bid?: $")

  data_dictionary["name"] = input_name
  data_dictionary["bid"] = input_bid
 
  print(data_dictionary)
  data_host.append(data_dictionary.copy())
  
  bid_choice = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  #clear()
print(data_host)