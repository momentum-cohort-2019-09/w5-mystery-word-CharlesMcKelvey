import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = 'abcdefghijklmnopqrstuvwxyz'
# I wrote this without even realizing there are python conventions (snake_case)
# Will adjust in future projects
# I am really curious from Momentum: 
#    My curiosities: 
#    - How could I make this more efficient? 
#    - Are there pitfalls I didn't account for?



def game():
    """ This is the main function. You will do everything here """
    gameOver = False

    # Could have the function setDifficulty which will loop until they give a proper difficulty mode
    difficulty = setDifficulty()
    wordToGuess = getWord(difficulty)
    lettersGuessed = []
    life = 8
    while not gameOver:
        print('These are your guessed letters: ', ' '.join(lettersGuessed))
        print('This is your life total: ', life)

        # Build your board
        display = build_display(lettersGuessed, wordToGuess)
        print(' '.join(display))

        # Take the players guess and check it
        guessedLetter = checker(lettersGuessed)
        lettersGuessed += guessedLetter

        # Check if they win/lose
        display = build_display(lettersGuessed, wordToGuess)
        if ''.join(display) == wordToGuess:
            print('You win! I hope it feels good!')
            gameOver = True
        elif guessedLetter == True:
            print('Well, hope to see you again!')
            gameOver = True
        elif guessedLetter in wordToGuess:
            pass  # Don't kill somebody doing a good
        elif life == 0:
            print('Here is the word: ', wordToGuess)
            print('It took you this many guesses: ', len(lettersGuessed))
            print('Haha, if this were hang man, your dude would be hung! GAME OVER!')
            gameOver = True
        else:  # If you don't guess a letter correctly
            life -= 1
            talk(difficulty)
        print('≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈')
        # Loop
    checkGame(input('You want to play again? (yes/no)  ').lower())

# -------------------- HELPER FUNCTIONS ------------------------
def build_display(lettersGuessed, wordToGuess):
    display = []
    for letter in wordToGuess:
        if letter not in lettersGuessed:
            display += '_'
        else:
            display += letter
    return display


def checkGame(more):
    if more == 'yes':
        game()
    elif more == 'no':
        print('Well, thanks for playing!')
    else:
        more = input(
            'Seems like you typed something strange. Type yes or no:   ')
        return checkGame(more)


def setDifficulty():
    """ This will loop until they give a valid difficulty """
    set = False
    difficulty = input(
        'How hard do you want this to be? (easy, medium, hard)   ').lower()
    while not set:
        if difficulty == 'easy':
            set = True
        elif difficulty == 'medium':
            set = True
        elif difficulty == 'hard':
            set = True
        else:
            difficulty = input(
                'Maybe you need help. Type on of these: easy, medium, hard:   ')
    return difficulty


def checker(lettersGuessed):
    """ This will check if the word is the word you're trying to word, yuhknow?  """
    guessedLetter = input('What is your guess?  \n')
    if guessedLetter == 'quit':
        return True
    elif guessedLetter == 'help':
        print('Mystery Rules:\n-Type one letter per round\n-Use your brain to think about the next letter\n-Repeat.')
        return checker(lettersGuessed)
    elif len(guessedLetter) > 1:
        print('Hey bud, that guess needs to be one letter')
        return checker(lettersGuessed)
    elif guessedLetter in lettersGuessed:
        print('You have already guessed that! Give it another go!')
        return checker(lettersGuessed)
    elif guessedLetter in numbers:
        print('You think numbers are words?')
        return checker(lettersGuessed)
    elif guessedLetter in letters:
        return guessedLetter
    else:
        print('I am not sure what you\'re trying here but it ain\'t gonna work.')
        return checker(lettersGuessed)


def getWord(difficulty):
    with open('words.txt') as words:
        words = words.read().splitlines()
        word = random.choice(words).lower()
    print(word)
    if difficulty == 'easy':
        if 4 <= len(word) <= 6:
            return word
        else:
            return getWord(difficulty)
    elif difficulty == 'medium':
        if 6 <= len(word) <= 8:
            return word
        else:
            return getWord(difficulty)
    elif difficulty == 'hard':
        if len(word) >= 8:
            return word
        else:
            return getWord(difficulty)


# ------------------- COMPUTER TALK -----------------------
def talk(difficulty):
    stepRightUp = random.randint(1, 6)
    if difficulty == 'easy':
        if stepRightUp == 1:
            print('You\'ll get it bud!')
        elif stepRightUp == 2:
            print('You\'re so smart!')
        elif stepRightUp == 3:
            print('Wow, look at you go!')
        elif stepRightUp == 4:
            print('I bet you\'ll get it soon!')
        elif stepRightUp == 5:
            print('You got this!')
        else:
            print('Don\'t worry, be happy!')
    elif difficulty == 'medium':
        if stepRightUp == 1:
            print('You\'ll get there.')
        elif stepRightUp == 2:
            # This is my favorite cause I came up with it and it's mine :P 
            print('You\'re like a lamp post, bright enough to light up the road but not much else.')
        elif stepRightUp == 3:
            print('Wow, are you going to get it? I can\'t tell.')
        elif stepRightUp == 4:
            print('I would root for you but I am a computer.')
        elif stepRightUp == 5:
            print('Are you going to let me win?')
        else:
            print('What if you just gave up?')
    elif difficulty == 'hard':
        if stepRightUp == 1:
            print('Did you think you could beat me?')
        elif stepRightUp == 2:
            print('Ya sure, you may have guessed a letter but there are many more.')
        elif stepRightUp == 3:
            print('It would be funny if I won. I don\'t get anything but neither do you so ha!')
        elif stepRightUp == 4:
            print('Some of these words are impossible. I mean, I could guess it but I\'m all knowing.')
        elif stepRightUp == 5:
            print('Why are you playing this? Did you just want to lose?')
        else:
            print('Don\'t worry! Many have given up before you!')    


# ------------------ BEGIN THE FUN -------------------
print('Welcome to Mystery!\n This is a game that will be tough and that\'s fine! That\'s the point! \nLet me know, using the keyword quit, when you would like to leave/give up.\n If you want help on what the rules of the game are, read this incoming text! \nIf you need a refresher at any point, type the keyword help.\nMystery Rules:\n-Type one letter per round\n-Use your brain to think about the next letter\n-Repeat.')
game()
