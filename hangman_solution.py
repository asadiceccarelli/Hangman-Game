import random


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.word_list = word_list
        self.num_letters = set([i for i in self.word])
        self.num_lives = num_lives
        self.list_letters = []
        self.visual = {
            5: f'__________\n  |      |\n  |\n  |\n  |\n__|____ ',
            4: f'__________\n  |      |\n  |      O\n  |\n  |\n__|____',
            3: f'__________\n  |      |\n  |      O\n  |      |\n  |\n__|____',
            2: f'__________\n  |      |\n  |      O\n  |      |\n  |     /\n__|____',
            1: f'__________\n  |      |\n  |      O\n  |      |\n  |     / \\\n__|____',
            0: f'__________\n  |      |\n  |    \ O /\n  |      |\n  |     / \\\n__|____'
        }

        print(f'The mystery word has {len(self.word)} characters.')
        print(self.word_guessed)


    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        '''
        word_split = [i for i in self.word]

        if letter.lower() in word_split:
            while letter.lower() in word_split:
                occurance = word_split.index(letter.lower())
                self.word_guessed[occurance] = letter.lower()
                word_split[occurance] = '_'
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
            print(self.visual[self.num_lives])
            return
    
        print(f'Nice! {letter} is in the word!')
        print(self.word_guessed)
        self.num_letters.remove(letter)
        return
        

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        valid_letter = False
        while valid_letter == False:
            letter = input('Enter a letter and press enter: ')
            if len(letter) != 1:
                print('Please, enter just one character')
            elif letter in self.list_letters:
                print(f'{letter} has already been tried.')
            else:
                valid_letter = True
        
        self.list_letters.append(letter)
        self.check_letter(letter)


def play_game(word_list):
    '''
    Function to play a single game.
    '''
    game = Hangman(word_list, num_lives=5)
    
    while game.num_lives > 0:
        game.ask_letter()
        if len(game.num_letters) == 0:
            print(f'Congratulations, you won! The word was \'{game.word}\'.')
            return
    else:
        print(f'You ran out of lives. The word was \'{game.word}\'.')
        return


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
