print("Please think of a number between 0 and 100!")

start = 0
end = 100
guessed = False

while not guessed:
    guess = int((start+end) /2)
    print("Is your secret number " + str(guess) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'l':
        start = int(guess)
    elif user_input == 'h':
        end = int(guess)
    elif user_input == 'c':
        break
        guessed = True
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(guess))