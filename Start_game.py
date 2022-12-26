import SwedishWordle
import Wordleboten


def start_game():

    game = SwedishWordle.Game()
    bot = Wordleboten.Wordle_Bot(game.the_word)
    
    
    while(game.num_guesses < 10):
        while True:
            try:
                result = game.Guess(input("Gissa ett ord på " + str(len(game.the_word)) + " antal bokstäver: "))
                break
            except ValueError:
                print("Felaktigt ord testa ett annat (Fel länge, otillåtet ord eller böjt ord")
        bot_result = bot.run_bot()
        print(result)
        player_win = victory_check(result)
        bot_win = victory_check(bot_result)
        if player_win == True:
            break
        if bot_win == True:
            break
    
    winner(player_win, bot_win)
    print("Ordet var: " + game.the_word)
    
    play_again = input("Vill du spela igen? ja/nej: ") 
    if play_again.lower() == "ja":
        start_game()
    else:
        pass


def victory_check(result):
    for r in result:
        if r == 0 or r == 1:
            return False  
    return True   


def winner(player_win, bot_win):
    if player_win and bot_win == True:
        print("Du spelade lika med boten!")
    elif player_win == True:
        print("Spelaren Vann!")
    elif bot_win == True:
        print("Boten Vann!")
    

def main():
    
    start_game()
        
        
    
    
if(__name__ == "__main__"):
    main()
