import gotypes
import goboard_slow
import agent.helpers

def main():
    player = gotypes.Player.black
    print(player.other)
    point = gotypes.Point(10, 10)
    print(point.neighbors())
    board = goboard_slow.Board(19, 19)
    board.place_stone(player, point)
    board.place_stone(player, gotypes.Point(2, 3))
    print(board._grid)
    state = goboard_slow.GameState.new_game(13)
    print(state.board.num_rows)

if __name__ == "__main__":
    main()
