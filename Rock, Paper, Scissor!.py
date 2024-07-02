import random


print("Rock, paper, Scissors! -- A Project by Interstellar2424")


RPS = ("rock", "paper", "scissors")
#RPS stands for rock, paper, scissors

player = input("choice (rock, paper, scissors): ")
AI = random.choice(RPS)


while player not in RPS:
    player = input("choice (rock, paper, scissors): ")


print(f"player: {player}")
print(f"AI: {AI}")


if player == AI:
    print("it's a tie")
elif player == "rock" and AI == "paper":
    print("You Lose!")
elif player == "paper" and AI == "pcissors":
    print("You Lose!")
elif player == "scissors" and AI == "rock":
    print("You lose!")

else:
    print("You Won!")
