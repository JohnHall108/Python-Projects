low = 0
high = 100

print("Please think of a number between 0 and 100! \n\n")
while True:
    guess = (high + low)//2
    print("Is your secret number " +str(guess)+"? \n")
    a=input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly. \n\n >>>>")
    if a == "c":
        print("Game over. Your secret number was: ", (guess))
        break
    elif a == "l":
        low=guess
    elif a == "h":
        high=guess
    else:
        print("Sorry, I did not understand your input. \n >>>>")