import unittest
from tennis import game


class TestTennis(unittest.TestCase):
    actual_score = ""

    def setUp(self):
        self.actual_score = "";

    def board(self, score):
        self.actual_score += score + "\n"

    def test_tennis_player1_win_a_sentence(self):
        expected_score = """0-0 (0:0)
15-0 (0:0)
30-0 (0:0)
40-0 (0:0)
player 1 won (0:0)
0-0 (1:0)
"""
        g = game(self.board)
        g.send(1)
        g.send(1)
        g.send(1)
        g.send(1)
        self.assertEqual(expected_score, self.actual_score)

    def test_tennis_player2_win_a_sentence(self):
        expected_score = """0-0 (0:0)
0-15 (0:0)
0-30 (0:0)
0-40 (0:0)
player 2 won (0:0)
0-0 (0:1)
"""
        g = game(self.board)
        g.send(2)
        g.send(2)
        g.send(2)
        g.send(2)
        self.assertEqual(expected_score, self.actual_score)

    def test_tennis_players_go_1_1(self):
        expected_score = """0-0 (0:0)
15-0 (0:0)
30-0 (0:0)
40-0 (0:0)
player 1 won (0:0)
0-0 (1:0)
0-15 (1:0)
0-30 (1:0)
0-40 (1:0)
player 2 won (1:0)
0-0 (1:1)
"""
        g = game(self.board)
        g.send(1)
        g.send(1)
        g.send(1)
        g.send(1)
        g.send(2)
        g.send(2)
        g.send(2)
        g.send(2)
        self.assertEqual(expected_score, self.actual_score)

    def test_tennis_long_game(self):
        expected_score = """0-0 (0:0)
15-0 (0:0)
30-0 (0:0)
40-0 (0:0)
40-15 (0:0)
40-30 (0:0)
deuce (0:0)
advantage player 1 (0:0)
deuce (0:0)
advantage player 2 (0:0)
deuce (0:0)
advantage player 1 (0:0)
player 1 won (0:0)
0-0 (1:0)
"""

        g = game(self.board)
        g.send(1)
        g.send(1)
        g.send(1)
        g.send(2)
        g.send(2)
        g.send(2)
        g.send(1)
        g.send(2)
        g.send(2)
        g.send(1)
        g.send(1)
        g.send(1)
        self.assertEqual(expected_score, self.actual_score)


if __name__ == '__main__':
    unittest.main()
