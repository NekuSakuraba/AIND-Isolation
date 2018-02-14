"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from game_agent import custom_score, custom_score_2

from sample_players import *

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer(score_fn=improved_score, name='Improved Score')
        self.player2 = game_agent.AlphaBetaPlayer(score_fn=custom_score, name='Custom Score 1')
        # self.player2 = RandomPlayer()
        # self.player2 = GreedyPlayer()
        # self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        print('Started!')
        scores = {self.player1: 0, self.player2: 0}

        for i in range(100):
            game = isolation.Board(self.player1, self.player2)
            winner, history, outcome = game.play(150)
            print('#{} {} - {}'.format(i, winner, outcome))
            scores[winner] += 1

            # print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
            # print(game.to_string())
            # print("Move history:\n{!s}".format(history))

        print('SUMARY')
        print(scores)


if __name__ == '__main__':
    unittest.main()
