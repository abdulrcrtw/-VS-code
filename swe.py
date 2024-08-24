print("Welcome to my job interview")

job = input("What kind of job are u looking for: ")
print(job)
if job != "Adidas":
    print("Sorry we are not the right place for you but carry on with the interview we would like to see how bad you are ")
else:
    print("Very well then u can now proceed with the interview! ")
score = 0

answer = input("How many kits in the premier league does adidas manufacture? ")
if answer == "Five":
    print("Correct ")
    score += 1 
else:
    print("Wrong! Adidas does not manufacture " + answer + " kits we only manufacture Five ") 

answer = input("Where does the name adidas originate from? ")
if answer == "From the name of the original creator of the company ":
    print("Correct ")
    score += 1
else:
    print("Wrong! Adidas was formed from the name Addidasler the original creator and owner of the company ")

answer = input("Which country does the company originate from ")
if answer == "Germany":
    print("Correct ")
    score += 1 
else: 
    print("Wrong! The company originally originates from germany ")
    
answer = input("Who is adidas main competitor in every sport ")
if answer == "Puma":
    print("Correct nike is not regarded as a competitor but as a watchdog to our greatness ")
    score += 1 
else : 
    print("Wrong! nike is not regarded as a competitor but as a watchdog to our greatness ")

print("You got " + str(score) + " questions correctly ")
if score != "Two":
    print("You have failed the interview seek mykhalo mudryk as help ")
else:
    print("Welcoe to adidas")