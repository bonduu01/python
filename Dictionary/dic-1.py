programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
  "num": 90,
}

def print_programming():
  for thing in programming_dictionary:
    print(programming_dictionary[thing])
    print(thing)

#print_programming()

capitals = {
  "Nigeria": "Lagos",
  "Ghana": "Accra",
  "Egypt": "Cario",
}

travel_log = {
  "Nigeria": ["Delta", "Lagos", "Abuja"],
  "Ghana": ["Accra", "Kumasi"],
  "Egypt": ["Cario", "Suez"]
}

cities_visited = {
  "Nigeria": {"cities visited": travel_log, "Total visits": 100},
  "Ghana": travel_log
}
def print_capitals():
  for capital in capitals:
    print(capital)

def print_state():
  for state in capitals:
    print(capitals[state])

#print_capitals()
#print_state()

def print_travel_log():
  for travel in travel_log:
    print (travel_log[travel])

#print_travel_log()

def print_cities_visited():
  for city in cities_visited:
    print(cities_visited[city])

#print_cities_visited()

employee_bio_data = [
{
  "fullname": "Peter",
  "job_role": "DevOps",
  "age": 39
},
{
  "fullname": "Tope",
  "job_role": "Ui/UX",
  "age": 33
},
]

#print(employee_bio_data)
for employee in employee_bio_data:
  print(employee)