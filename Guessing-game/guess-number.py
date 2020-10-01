import random
a=int(input("enter a number to get guessing number between  them"))
n = random.randrange(a)
number_of_guesses=1
print("Number of guesses is limited to only 6 times: ")
print("guess the number below ", a)
while (number_of_guesses<=6):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<n:
        print("you enter less number please enter greater number.")
    elif guess_number>n:
        print("you enter greater number please enter smaller number.")
    else:
        print("Game Over")
        print("you won")
        print("no of guesses you took to finish the game is", number_of_guesses)
        break
    print(6-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>6):
    print("the number is", n,)
    print("Game Over")
    print("you Lose")
