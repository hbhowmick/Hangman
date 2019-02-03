from IPython.display import clear_output
import time
import random
class Hangman():
    def __init__(self):
        self.categories = {'sports':['baseball','football','hockey','softball','soccer','cricket','rugby','lacrosse'],
                          'colors':['red','orange','yellow','green','blue','purple','black'],
                           'flowers':['daisy', 'tulip', 'rose', 'iris', 'hydrangea', 'snapdragon', 'lily', 'carnation'],
                           'cities':['Boston', 'London', 'Paris', 'Singapore', 'Delhi', 'Dublin', 'Berlin', 'Bogota',
                                     'Havana', 'Miami', 'Chicago', 'Beijing', 'Rome', 'Cairo', 'Sydney', 'Melbourne',
                                     'Moscow', 'Tokyo', 'Dubai', 'Johannesburg']
                          }
        self.category = ''
        self.word_to_guess = ''
        self.guesses = []
        self.lives = 5
        self.flag = True

    def printInstructions(self):
        print('Welcome to Hangman! Guess a word - you have 5 lives before you are hung out to dry!')

    def printCategories(self):
        print('\n\nHere are the categories:')
        for k in self.categories.keys():
            print(k.title())

    def pickCategory(self):
        self.flag=True
        while True:
            self.printCategories()
            self.category = input('What category would you like to pick? ')
            if self.category in self.categories:
                clear_output()
                print('\nYou\'ve chosen {}!\nLet\'s play!'.format(self.category.upper()))
                break
            else:
                clear_output()
                if self.category.lower() == 'quit':
                    break
                else:
                    print('\n***{} is not a valid category***'.format(self.category))

    def chooseWord(self):
        self.word_to_guess = random.choice(self.categories[self.category])

    def showSpaces(self):
        self.string = (('_ ')*len(self.word_to_guess))
        print(self.string)

    def showStatus(self, aList):
        self.guesses=aList
        guessed_status = ''
        for i in range(len(self.word_to_guess)):
            letter_to_guess = self.word_to_guess[i].lower()
            if letter_to_guess in self.guesses:
                guessed_status += letter_to_guess + ' '
            else:
                guessed_status += '_ '
            self.guessed_status = guessed_status
        print('\nCategory: {}\n'.format(self.category.upper()))
        print(self.guessed_status)
        print('\nGuesses: ')
        print(''.join(self.guesses))
        if '_' not in self.guessed_status:
            print('\nYOU WIN!!!')
            self.flag=False

    def checkLetter(self):
        time.sleep(0.02)
        while self.flag==True:
            time.sleep(0.02)
            letter = input('\nGuess a letter: ')
            if letter == 'quit':
                break
            elif len(letter) > 1:
                print('Guess one letter at a time...')
                continue
            elif letter in self.word_to_guess.lower():
                self.guesses.append(letter)
                clear_output()
                print('\nCorrect! Remaining lives: {}\n'.format(self.lives))
            else:
                self.guesses.append(letter)
                self.lives -= 1
                if self.lives==0:
                    clear_output()
                    print('\nGame over :(\n')
                    print(self.guessed_status)
                    print('\nGuesses: ')
                    print(''.join(self.guesses))
                    break
                else:
                    clear_output()
                    print('\nSorry, try again! Remaining lives: {}\n'.format(self.lives))
            self.showStatus(self.guesses)

    def checkComplete(self):
        if '_' in self.string:
            self.checkLetter()


game = Hangman()


while True:
    game.guesses = []
    game.lives = 5
    game.printInstructions()
    time.sleep(0.02)
    game.pickCategory()
    game.chooseWord()
    game.showSpaces()
    game.checkLetter()
    time.sleep(0.02)

    ans = input('Play another game?(y/n) ')
    if ans == 'n':
        break
    else:
        clear_output()
