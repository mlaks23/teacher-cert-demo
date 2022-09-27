import random

def play():
    user = input("Choose r for rock, p for paper or s for scissors: ")
    computer = random.choice(["r", "p", "s"])
    print("You chose " + user)
    print("The computer chose " + computer)

    if user == computer:
        return("It's a tie.")

    elif is_win(user, computer):
        return("You won.")
    
    else:
        return("You lost.")
    
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())