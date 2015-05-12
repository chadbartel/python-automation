# This is a guess the number game.
import random
secret_num = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_num:
        print('Your guess is too low.')
    elif guess > secret_num:
        print('Yor guess is too high.')
    else:
        break   # This condition is the correct guess!

if guess == secret_num:
    print('Good job! You guess my number in ' + str(guess_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_num))
