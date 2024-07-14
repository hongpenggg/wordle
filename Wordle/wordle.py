# game file

from random import choice


# game class
class Wordle:
    '''
    Class: Wordle
    ---------------------------------------------------------
    Description: A simple word game where the user has to guess a word of length 5
    ---------------------------------------------------------
    Methods:
    - __init__(): Initialises the game
    - all_words(): Extracts all words from a text file
    - valid(): Validates user input
    - check_guess(): Checks if the user's guess is correct
    - display(): Displays the board
    - prompt(): Prompts the user for input
    - main(): Runs the game
    ---------------------------------------------------------
    Attributes:
    - word: The word to be guessed
    - count: The number of guesses
    - board: The board to display the word
    - dict: The dictionary of words
    - past_guesses: The list of past guesses
    ---------------------------------------------------------
    '''
    
    def __init__(self):
        self.word = choice(self.all_words())
        self.count = 0
        self.board = [[] for i in range(len(self.word))]
        self.dict = self.all_words()
        self.past_guesses = []
        print('Wordle game initialised.')
    

    # extract words
    def all_words(self):
        with open('words.txt', 'r') as f:
            r = f.readlines()
            r = [r[i][:-1:] for i in range(len(r))]
            
            return r


    # user input validation
    def valid(self, guess):
        if len(guess) != 5:
            return "Word must be of length 5!"
        
        if guess.isalpha() == False:
            return "Word must contain only alphabetical characters!"
        
        return True if guess in self.dict else "Word not found!"


    # check guess
    def check_guess(self, guess, word):
        self.board = [[] for i in range(len(self.word))]
        matched_letters = []

        if guess == word:
            return True
        else:
            letters = [guess[i] for i in range(len(guess))]

            for i in range(len(letters)):
                if letters[i] == word[i]:
                    self.board[i] = [letters[i]]
                    matched_letters.append(letters[i])
                elif letters[i] in [word[i] for i in range(len(word))]:
                    if letters.count(letters[i]) <= word.count(letters[i]) and matched_letters.count(letters[i]) < word.count(letters[i]):
                        self.board[i] = [f'_{letters[i]}_']
                        matched_letters.append(letters[i])

            return self.board


    # display guess + word
    def display(self):
        print(self.board)


    # prompt user for inputs
    def prompt(self):
        print(f"Tries Left: {6 - self.count}")
        guess = input("Enter your guess: ")
        return guess


    # run game
    def main(self):
        print("Welcome to the wordle.")
        print("Your board will be displayed like: [h][e][l][l][o]")
        print("At the start, your board is empty, so it will be: [][][][][].")
        print("After each guess, if you guessed a letter a the right place, that letter will appear in the box: [h][e][l][l][o]")
        print("If the letter is right but not in the right place, it will be underlined: [h][_a_][l][l][o]")
        print("If the letter isn't in the word, it won't appear in the box: [][e][l][l][o]")
        print()
        self.display()

        correct = False

        while correct != True and self.count < 7:
            print()
            g = self.prompt()

            if g in self.past_guesses:
                print(f"Hey, you've guessed {g} already!")
                print("Try another word!")
                print()
                self.display()
                correct = False
                self.board = [[] for i in range(len(self.word))]
                continue

            if self.valid(g) == True:
                self.count += 1
                self.past_guesses.append(g)

                if self.check_guess(g, self.word) == True:
                    print("Correct!")
                    self.board = [[g[i]] for i in range(len(g))]
                    print(self.board)
                    print()
                    correct = True
                
                else:
                    print()
                    self.display()
                    correct = False
                    self.board = [[] for i in range(len(self.word))]

                    if self.count > 5:
                        print()
                        print("Oops, you didn't get the word in 6 guesses.")
                        print(f"The word was: {self.word}")
                        break

            else:
                print(self.valid(g))
                print()
                self.display()
                correct = False
                self.board = [[] for i in range(len(self.word))]
            
        self.board = [[] for i in range(len(self.word))]
        print("Play again tomorrow!")
        print("Exiting game...")


a = Wordle()
# print(a.word)
a.main()
