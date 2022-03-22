#Guess the number game.
#Goal: user should guess the number having the five attempts.
import random

guessesTaken = 0
print("Hello! What's yo name?")
userName = input()

numberToGuess = random.randint(1,101)

print("Well, " + userName + ", I'm thinking of a number between 1 and 101")

for guessesTaken in range(5):
    print("Take a guess:")
    guess = input()
    guess = int(guess)

    if guess > numberToGuess:
        print("Your guess is to high.")

    if guess < numberToGuess:
        print("Your guess is too low.")

    if guess == numberToGuess:
        break

if guess == numberToGuess:
    guessesTaken = str(guessesTaken + 1)
    print("Gj, " + userName + "! You guessed ma numba just in " + guessesTaken + " guesses!")

if guess != numberToGuess:
    numberToGuess = str(numberToGuess)
    print("Nope. Not today buddy, the number I was thinking is " + numberToGuess)
