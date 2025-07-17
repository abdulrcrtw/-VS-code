import random 


def roll():
    min_value = 1
    max_value = 6 
    return random.randint(min_value, max_value)
    


while True:
    players = input("Enter the number of players (2 - 4 ): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players ")
    else:
        print("Invalid try again ")
        
max_score = 50 
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players): 
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        current_score = 0 
        
    while True:
        should_roll = input("Would you like to roll the dice? (y/n): ")
        if should_roll != "y":
            break
        
        value = roll()
        print("You rolled a", value)
        
        if value == 1:
            print("Oh no! You rolled a 1. Turn over, no points added.")
            current_score = 0
            break 
        else:
            current_score += value 
            print("Current turn score:", current_score)
    
    player_scores[player_idx] += current_score
    print(f"Total score for player {player_idx + 1}: {player_scores[player_idx]}")
    
    if player_scores[player_idx] >= max_score:
        print(f"\nPlayer {player_idx + 1} wins with a score of {player_scores[player_idx]}!") 
    
    else:
        continue
    break            