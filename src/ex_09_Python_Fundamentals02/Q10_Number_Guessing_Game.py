counter=0
while(True):
    myGuess=10
    guess=int(input("Guess:"))
    counter+=1
    if(guess==myGuess):
        print("You guessed right!")
        print("In ",counter," tries")
        break
    elif(guess>myGuess):
        print("Too High!")

    elif(guess<myGuess):
        print("Too Low!")


