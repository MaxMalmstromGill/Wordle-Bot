import random
import SwedishWordle

class Wordle_Bot(object):
    
    def __init__(self, the_word):
        self.bot_game = SwedishWordle.Game()
        self.bot_game.the_word = the_word
        self.possible_words = self.bot_game.words_in_game


    def run_bot(self):
        self.result = self.bot_game.Guess(self.guess())
        self.word_remover()
        return self.result


    def guess(self):
        self.bot_guess = random.choice(self.possible_words)
        print("Boten gissade från en lista på " + str(len(self.possible_words)) + " ord")

        return self.bot_guess


    def remove_word(self, letter): 
        for word in list(self.possible_words):
            if letter in word:
                self.possible_words.remove(word)
                
    
    def remove_word_by_letter_position(self, letter, letter_index):
        for word in list(self.possible_words):
            if letter != word[letter_index]:
                self.possible_words.remove(word)
    

    def remove_word_by_wrong_letter_position(self, letter, letter_index):
        for word in list(self.possible_words):
            if letter == word[letter_index]:
                self.possible_words.remove(word)
            if letter not in word:
                self.possible_words.remove(word)
                
                
    def word_remover(self):
        for i, r in enumerate(self.result):
            if r == 2:
                self.remove_word_by_letter_position(self.bot_guess[i], i)
                
            elif r == 1:
                self.remove_word_by_wrong_letter_position(self.bot_guess[i], i)
                 
            else:
                self.remove_word(self.bot_guess[i])
