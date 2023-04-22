#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
final_choice = True
data_dictionary = {}
bid_choice = "yes"
data_host = []
num = 0
name = ''
bid_winner = {}
winner = []
while bid_choice == "yes":
  #data_dictionary{}
  input_name = input("What is your name?: ")
  input_bid = int(input("What's your bid?: $"))

  data_dictionary["name"] = input_name
  data_dictionary["bid"] = input_bid
  
  if input_bid > num:
      bid_winner["name"] = input_name
      bid_winner["bid"] = input_bid
      num = input_bid
 
  print(data_dictionary)
  data_host.append(data_dictionary.copy())
  
  bid_choice = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  
  #clear()
#print(data_host)
print (bid_winner)

