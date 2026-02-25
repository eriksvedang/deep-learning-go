import gotypes
import goboard_slow

def main():
    player = gotypes.Player.black
    print(player.other)
    point = gotypes.Point(10, 10)
    print(point.neighbors())
    board = goboard_slow.Board(19, 19)
    board.place_stone(player, point)
    board.place_stone(player, gotypes.Point(2, 3))
    print(board._grid)

if __name__ == "__main__":
    main()
