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

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        
        
    guesses += 1 
    
    if user_guess == random_number:
        print("You got it right!")
        print(f"It took you {guesses} guesses.")
        quit()
    
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number")
        quit()
