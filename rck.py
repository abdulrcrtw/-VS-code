import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, try again. ")
        
max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn!")
        current_score = 0 
        
    while True:
        should_roll = input("Roll the dice? (y/n): ").lower()
        if should_roll != "y":
            break
        
        value = roll()
        if value == 1:
            print("You rolled a 1! No points this turn.")
            current_score = 0
            break 
        else:
            current_score += value
            print(f"You rolled a {value}. Current turn score: {current_score}")
            
    player_scores[player_idx] += current_score
    print(f"Player {player_idx + 1}'s total score: {player_scores[player_idx]}")
    
    if player_scores[player_idx] >= max_score:
        print(f"\n Player {player_idx + 1} wins with {player_scores[player_idx]} points!")
        break 