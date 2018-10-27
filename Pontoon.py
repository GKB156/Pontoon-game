low = 0
high = 100
guess = (high + low)//2

print("Please think of a number between 0-100!")
print("Is your secret number " + str(guess) + "?")
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")   
while ans != "c":
    if ans == "h":
        high = guess
        guess = (high + low)//2
    elif ans == "l":
        low = guess
        guess = (high + low)//2      
    else:
        print("Sorry, I didn't understand your input")
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")    
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 

print("Game over. Your secret number was: " + str(guess))
