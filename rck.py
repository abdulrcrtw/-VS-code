import random

def play():
   user = input("What's your choice? 'r' for rocks, 'p' for paper, 's' for scissors\n ")
   computer = random.choice (['r' 'p' 's'])
   
   if user == computer:
       return "Its a tie"

   if is_win(user,computer):
       return "You won!" 
   else:
       return "You lost!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or (player == 'p' and opponent == 'r'):
        return True 
    

print(play())    