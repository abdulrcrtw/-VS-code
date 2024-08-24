import random 

top_of_range = input("Type a number: " )

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type in a number larger than 0 next time ")
        quit()

else:
    print("Please type a number larger than 0 next time ")
    quit()

random_numbeer = random.randint(0, top_of_range)

while True:
    user_guess = input("Make a guess: ")
  

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type in a number larger than 0 next time ")
        quit()

else:
    print("Please type a number larger than 0 next time ")
    quit()
