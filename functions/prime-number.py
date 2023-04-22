def prime_checker(number):
    prime = None
    small_num = []
    numbers = []
    if number < 1:
        number == 1

    for position in range(1, number):
        numbers.append(number%position)
        
    if numbers.count(0) == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
