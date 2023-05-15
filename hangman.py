import random
import sys


def main():
    ''' The main function'''
    start()
    
    
def start():
    '''Runs game'''
    
    # Welcome
    print("Welcome to Hangman\n")
    print("Loading word...")
    
    # Loads a random word
    word = get_word()
    length = len(word)
    print("Word to be guessed", end="\t")
    
    # Prints the dashed line
    print('_'* length)
    
    
    # TO-DO
    # now you need to some how accept a letter every iteration(provided with get_letter function)
    # And then you need to display the current string(with found charecters and dashes)
    # use disp function
    
    
def disp(word: str, current: str, guess: str) -> str: 
    
    # takes as input 3 strings the first is the word like (hello), the second is the current guess like( h_llo) and the third is the letter like(e)
    # you need to display the current orientation, update with new letters and then finnaly exit game if game is over
    ...

def get_letter():
    while True:
        letter = input("Enter letter: ")
        if len(letter) == 1:
            print('read letter', letter)
            return letter

def get_word():
    '''Gets Word'''
    # Random word gen
    from random_word import RandomWords 
    r = RandomWords()
    
    while True:
        word = r.get_random_word()
        if len(word) < 5:
            return word

def printlogo():
    logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

    print(logo)

def hangman(lives: int):
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    
    try:
        stage = 8 - lives
        print(stages[stage])
    except IndexError:
        print(stages[-1])

def clear_terminal():
    # ANSI escape sequence to clear the terminal screen
    sys.stdout.write("\033c")
    sys.stdout.flush()


if __name__ == "__main__":
    main()