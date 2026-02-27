import dlgo.gotypes
from dlgo.goboard import GameState
from dlgo.agent.naive import RandomBot
from dlgo.minmax.minmax import MinMaxBot
from dlgo.montecarlo.montecarlo import MCTSAgent
from dlgo.utils import print_board, print_move, point_from_coords
from dlgo.gotypes import Player
import time
import os

def play_vs():
    board_size = 7
    game = GameState.new_game(board_size)
    players = {
        Player.black: MCTSAgent(50, 1.5),
        Player.white: MCTSAgent(50, 1.5),
    }
    while not game.is_over():
        #time.sleep(0.1)
        #os.system('clear')
        print_board(game.board)
        print('Black captures: %d' % game.board.black_captures)
        print('White captures: %d' % game.board.white_captures)
        print('Diff: %d' % game.capture_diff())
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
    result = dlgo.scoring.compute_game_result(game)
    print("Winner: %s (margin %i)" % (result.winner, result.winning_margin))

def main():
    play_vs()

if __name__ == "__main__":
    main()
