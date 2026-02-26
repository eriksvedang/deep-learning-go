import random
import enum
from dlgo.agent.base import Agent
from dlgo.agent.helpers import is_point_an_eye
from dlgo.goboard import Move
from dlgo.gotypes import Point

class MinMaxBot(Agent):
    def select_move(self, game_state):
        best_moves = []
        best_score = MIN_SCORE

        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = best_result(next_state, max_depth=4)
            our_best_outcome = -1 * opponent_best_outcome
            print('Possible move %s (%s) has best outcome %d' % (possible_move, game_state.next_player, our_best_outcome))
            if (not best_moves) or our_best_outcome > best_score:
                best_moves = [possible_move]
                best_score = our_best_outcome
            elif our_best_outcome == best_score:
                best_moves.append(possible_move)

        #print("Best moves: %s" % ", ".join(map(lambda m: str(m), best_moves)))
        return random.choice(best_moves)

MAX_SCORE = 99999
MIN_SCORE = -99999

def best_result(game_state, max_depth):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return MAX_SCORE
        else:
            return MIN_SCORE

    if max_depth == 0:
        return game_state.capture_diff()

    best_so_far = MIN_SCORE
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best = best_result(next_state, max_depth - 1)
        our_result = -1 * opponent_best
        if our_result > best_so_far:
            best_so_far = our_result
    return best_so_far
