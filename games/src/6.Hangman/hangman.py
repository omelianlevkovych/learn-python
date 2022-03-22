# libraries
import random

# Assert ASCII art
HANGMAN_PICTURES = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
0   |
    |
    |
   ===''', '''
+---+
0   |
|   |
    |
   ===''', '''
+---+
0   |
/|  |
    |
   ===''', '''
+---+
 0  |
/|\ |
    |
   ===''', '''
+---+
 0  |
/|\ |
/   |
   ===''', '''
+---+
 0  |
/|\ |
/ \ |
   ===''']

WORDS = '''friend loss mechanism liability prince translate objective utter
reverse style dog shelf advocate migration think'''.split()

def getRandomWord(wordList):
    # This func returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICTURES[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace blanks with correcttly guessed letters.
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    # Show the secret word with spaces in between each letter.
    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered.
    # This func validate that the player entered a single letter.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have alraedy guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This func returns true if the player wans to play again;
    # otherwise, it returns false.
    print('Do you wanna play again? (yes or no)')
    return input().lower().startwith('y')


# The main function
print('H A N G M A N')
correctLetters = ''
missedLetters = ''
secretWord = getRandomWord(WORDS)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The secret word is "' +
                      secretWord + '" ! you have won!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICTURES) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' +
                  secretWord + '"')
            gameIsDone = True
        # Ask the player to play again
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(WORDS)
            else:
                break
                  
