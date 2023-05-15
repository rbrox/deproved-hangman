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
    word = get_word()
    length = len(word)
    print("Word to be guessed", end="\t")
    
    print('_'* length)
    
    
    # Dict to store the letters
    current = "_" * length
    
    # PLay 
    Lives = 8
    while Lives > 0:
        clear_terminal()
        printlogo()
        print('*'* 15)
        print('Current Lives =', Lives, end="\n\n")
        hangman(Lives)
        print(current)
        letter = get_letter()
        next = disp(word, current, letter)
        
        if next == current:
            Lives -= 1
        
        current = next
    
    print('GAME OVER')
    sys.exit()
    
def disp(word: str, current: str, guess: str) -> str: 
    
    new = ""
    for i in range(len(current)):
        if current[i] == '_' and word[i] == guess:
            new += word[i]
        else:
            new += current[i]
    
    if new == word:
        print('YOU WIN')
        sys.exit()
    
    return new
    

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