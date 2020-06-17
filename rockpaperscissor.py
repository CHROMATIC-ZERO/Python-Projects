import random, time
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
print("wins:", wins, "losses:", losses, "ties:", ties)
playagain =True
while playagain == True:
    #user choices
    userinp = input("What do you choose? (rock[r], paper[p], scissors[s]")
    if userinp == "r":
        print("ROCK VERSUS: ")
        time.sleep(2)
    elif userinp == "p":
        print("PAPER VERSUS: ")
        time.sleep(2)
    elif userinp == "s":
        print("SCISSOR VERSUS: ")
        time.sleep(2)
#computer choices
    compChoice = random.choice(["r", "p", "s"])

    if compChoice == "r":
        print("ROCK!")
    if compChoice == "p":
        print("PAPER!")
    if compChoice == "s":
        print("SCISSOR!")
### the outcomes:

    if userinp == compChoice:
        print("It's a DRAW!")
        ties = ties + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "r" and compChoice == "s":
        print("You WIN!")
        wins = wins + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "p" and compChoice == "r":
        print("You WIN!")
        wins = wins + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "s" and compChoice == "p":
        print("You WIN!")
        wins = wins + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "r" and compChoice == "p":
        print("You LOSE!")
        losses = losses + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "p" and compChoice == "s":
        print("You LOSE!")
        losses = losses + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
    elif userinp == "s" and compChoice == "r":
        print("You LOSE!")
        losses = losses + 1
        print("wins:", wins, "losses:", losses, "ties:", ties)
        ask = input("Play again?")
        if ask == "no":
            playagain = False
        else:
            playagain = True
