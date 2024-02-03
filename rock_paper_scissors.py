import random

user_wins = 0
pc_wins = 0

game = ["rock", "paper", "scissors"]

while True:
    user_input = input ("Type Rock/Paper/Scissors or q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in game:
        continue
    
    random_number = random.randint(0,2)
    
    pc_pick = game[random_number]
    print("PC picked", pc_pick + ".")
    
    if user_input == "rock" and pc_pick == "scissors":
        print ("You win!")
        user_wins += 1
    
    elif user_input == "paper" and pc_pick == "rock":
        print ("You win!")
        user_wins += 1
    
    elif user_input == "scissors" and pc_pick == "paper":
        print ("You win!")
        user_wins += 1
    
    else: 
        print("You lose!")
        pc_wins += 1
        
        
print ("You won", user_wins, "times")
print ("The PC won", pc_wins, "times")
print ("Adios!")
    
    