from distutils.ccompiler import new_compiler
import json
from mimetypes import guess_all_extensions
import os, sys
import random

all_swedish_words = None

class Game(object):


    def __init__(self, word_length = 5):
        with open(os.path.join(sys.path[0], 'svenska-ord.json')) as json_file:
            self.swedish_words = json.load(json_file)
        self.words_in_game = list(filter(lambda x: len(x)==word_length and "-" not in x and " " not in x, self.swedish_words))
        self.the_word = random.choice(self.words_in_game)  
        self.num_guesses = 0
           

    def Guess(self, word_guess):
        

        if len(word_guess) != len(self.the_word):
             raise ValueError(f"Felaktig längd på ord. Du gissade \"{word_guess}\". Detta spel är om ord som är {len(self.the_word)} i längd")

        if word_guess not in self.words_in_game:
             raise ValueError(f"Felaktigt ord. Du gissade \"{word_guess}\" vilket inte är ett ord i ordlistan.")
        
        result = []
        self.num_guesses += 1
        
        for index,letter in enumerate(word_guess):
            if letter == self.the_word[index]:
                result.append(2)
            elif letter in self.the_word:
                result.append(1)
            else:
                result.append(0)
                
        return result
