import unittest
from tennis import game


class TestTennis(unittest.TestCase):
    expected_score = """0-0
15-0
30-0
40-0
40-15
40-30
deuce
advantage player 1
deuce
advantage player 2
deuce
advantage player 1
player 1 won
"""

    actual_score = ""

    def board(self, score):
        self.actual_score += score + "\n"

    def test_tennis(self):
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
        self.assertEqual(self.actual_score, self.expected_score)


if __name__ == '__main__':
    unittest.main()
