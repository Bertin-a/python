import random

def get_choice():
    player_choice= input("Enter a choice(Rock, Paper,Scissors)")
    options =['rock','paper','scissors']
    computer_choice = random.choice(options)
    choices ={"player":player_choice, "computer":computer_choice}
    return choices
selections=get_choice()


def check_win(player,computer):
    print(f"You chose {player} and computer chose {computer}")
    if player==computer:
        return 'It is a tie'
    elif player=="rock":
        if computer=="scissors":
            return "Rock Smashes scissors! you win"
        else:
            return "paper covers rock you lose"
    elif player=="Paper":
        if computer=="scissors":
            return 'scissors cuts paper you lose'
        else:
            return  "paper covers rock you win"
    elif player=="scissor":
        if computer=="paper":
            return 'scissors cuts paper you Win'
        else:
            return  "Rock Smashes scissors, you lose"
    
        
check_win("rock","paper")
  








