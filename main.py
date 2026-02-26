import dlgo.gotypes
from dlgo.goboard import GameState
from dlgo.agent.naive import RandomBot
from dlgo.utils import print_board, print_move, point_from_coords
import time
import os

def play_vs():
    board_size = 19
    game = GameState.new_game(board_size)
    players = {
        dlgo.gotypes.Player.black: RandomBot(),
        dlgo.gotypes.Player.white: RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.0)
        os.system('clear')
        print_board(game.board)
        print('')
        player = players[game.next_player]
        if player is None:
            human_input = input('-- ').upper()
            point = point_from_coords(human_input.strip())
            move = dlgo.goboard.Move.play(point)
        else:
            move = player.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)

def main():
    play_vs()

if __name__ == "__main__":
    main()
