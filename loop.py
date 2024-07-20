print("Welcome to my quiz game ")

playing = input("Do u want to play? ")
print(playing)
if playing.lower() != "yes":
    quit()
else:
    print("Let's play")
score = 0    

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Wrong! ")

answer = input("Who is the best footballer on the planet? ")
if answer.lower() == "lionel messi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("How many football clubs are in the premier league? ")
if answer.lower() == "twenty":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What is the capital of Hungary? ")
if answer.lower() == "budapest":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("You got " + str(score) + " questions correctly")
    