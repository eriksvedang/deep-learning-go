import dlgo.gotypes
from dlgo.goboard import GameState
from dlgo.agent.naive import RandomBot
from dlgo.print_utils import print_board, print_move
import time
import os

def bot_vs_bot():
    board_size = 19
    game = GameState.new_game(board_size)
    bots = {
        dlgo.gotypes.Player.black: RandomBot(),
        dlgo.gotypes.Player.white: RandomBot(),
    }
    while not game.is_over():
        #time.sleep(0.2)
        #print(chr(27) + "[2J")
        os.system('clear')
        print_board(game.board)
        print('')
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)

def main():
    bot_vs_bot()

if __name__ == "__main__":
    main()
