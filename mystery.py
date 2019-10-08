import random


def game():
    """ This is the main function. You will do everything here """
    gameOver = False

    # Could have the function setDifficulty which will loop until they give a proper difficulty mode
    difficulty = setDifficulty()

    if difficulty == 'easy':  # put into a function?
        # Grab from the text file at any random line, as well as checking the length of that word
        # This will only select words that are 4-6 characters long
        wordToGuess = getWord(difficulty)
        life = 8
        lettersGuessed = []

        print('Alright friend!')
        while not gameOver:
            print(lettersGuessed)
            display = []
            for letter in wordToGuess:
                if letter not in lettersGuessed:
                    display += '_'
                else:
                    display += letter
            print(' '.join(display))

            guessedLetter = checker()

            lettersGuessed += guessedLetter
            if (''.join(display) == wordToGuess):
                print('You win! I hope it feels good!')
                gameOver = True
            elif guessedLetter in wordToGuess:
                pass  # Don't kill somebody doing a good job
            elif life == 0:
                print('Haha, if this were hang man, your dude would be hung! GAME OVER!')
                gameOver = True
            else:  # If you don't guess a letter correctly
                cheerTalk()
                life -= 1
            print('This is your life total: ', life)

    elif difficulty == 'medium':
        # Grab from the text file at any random line, as well as checking the length of that word
        # This will only select words that are 6-8 characters long
        wordToGuess = getWord(difficulty)
        print('Alright sport!')
        while not gameOver:

            pass
    elif difficulty == 'hard':
        # Grab from the text file at any random line, as well as checking the length of that word
        # This will only select words that are 8+ characters long
        wordToGuess = getWord(difficulty)
        print('Alright fresh meat!')
        while not gameOver:
            pass
    else:
        print('I\'m not sure how you got here. This shouldn\'t be possible! Game Over!')
        gameOver = True

    startOverOrQuit = input('You want to play again? (yes/no)').lower()
    if startOverOrQuit == 'yes':
        game()
    elif startOverOrQuit == 'no':
        print('Well, thanks for playing. This was fun!')


# -------------------- HELPER FUNCTIONS ------------------------
def setDifficulty():
    """ This will loop until they give a valid difficulty """
    set = False
    difficulty = input(
        'How hard do you want this to be? (easy, medium, hard)').lower()
    while not set:
        if difficulty == 'easy':
            set = True
        elif difficulty == 'medium':
            set = True
        elif difficulty == 'hard':
            set = True
        else:
            difficulty = input(
                'Maybe you need help. Type on of these: easy, medium, hard:  ')
    return difficulty


def checker():
    """ This will check if the word is the word you're trying to word, yuhknow?  """
    guessedLetter = input('What is your guess?  ')
    if input ==


def getWord(difficulty):
    with open('words.txt') as words:
        words = words.read().splitlines()
        word = random.choice(words)
    if difficulty == 'easy':
        if len(word) <= 6:
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
def cheerTalk():
    ''' This will be used on easy mode '''
    stepRightUp = random.randint(1, 6)
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


def justTalk():
    ''' This will be used on medium mode '''
    stepRightUp = random.randint(1, 6)
    if stepRightUp == 1:
        print('You\'ll get there.')
    elif stepRightUp == 2:
        print('You\'re like a lamp post, bright enough to light up the road but not much else.')
    elif stepRightUp == 3:
        print('Wow, are you going to get it? I can\'t tell.')
    elif stepRightUp == 4:
        print('I would root for you but I am a computer.')
    elif stepRightUp == 5:
        print('Are you going to let me win?')
    else:
        print('What if you just gave up?')


def smackTalk():
    ''' This will be used on hard mode '''
    stepRightUp = random.randint(1, 6)
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
