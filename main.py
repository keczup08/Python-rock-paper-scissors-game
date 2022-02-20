import easygui as g
import random
import sys

choices = ["Rock", "Paper", "Scissors"]

if g.ccbox("Welcome to simple Rock, Paper, Scissors game in python!",):
    rounds = g.integerbox("How many rounds do you want to play?")
    rounds_played = 0
    score = 0

    while rounds != rounds_played:
        ai = random.choice(choices)
        g.msgbox("The computer chose something!")
        reply = g.buttonbox("Your choice:", choices=choices)
        rounds_played += 1

        if reply == "Rock" and ai == "Scissors":
            g.msgbox("Nice! you won round number: " + str(rounds_played))
            score += 1

        elif reply == "Scissors" and ai == "Paper":
            g.msgbox("Nice! you won round number: " + str(rounds_played))
            score += 1

        elif reply == "Paper" and ai == "Rock":
            g.msgbox("Nice! you won round number: " + str(rounds_played))
            score += 1

        elif reply == "Paper" and ai == "Scissors":
            g.msgbox("Oh no! you lost round number: " + str(rounds_played) + " The computer chose " + ai)

        elif reply == "Rock" and ai == "Paper":
            g.msgbox("Oh no! you lost round number: " + str(rounds_played) + " The computer chose " + ai)

        elif reply == "Scissors" and ai == "Rock":
            g.msgbox("Oh no! you lost round number: " + str(rounds_played) + " The computer chose " + ai)

        else:
            g.msgbox("Tie! Nobody wins!")

        if rounds_played == rounds:
            g.msgbox("GG! Thanks for playing! You won " + str(score) + " round/s out of " + str(rounds))
else:
    sys.exit()