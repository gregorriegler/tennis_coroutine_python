from coroutine import coroutine


def point_name(point):
    return ["0", "15", "30", "40"][point]


def score_as_string(score):
    if score[0] >= 3 and score[1] >= 3:
        if score[0] == score[1]:
            return "deuce"
        elif 2 > abs(score[0] - score[1]) > 0:
            if score[0] > score[1]:
                return "advantage player 1"
            else:
                return "advantage player 2"
        else:
            if score[0] > score[1]:
                return "player 1 won"
            else:
                return "player 2 won"
    elif score[0] <= 3 and score[1] <= 3:
        return point_name(score[0]) + "-" + point_name(score[1])


@coroutine
def game(board):
    score = [0, 0]
    while True:
        board(score_as_string(score))
        who_scored = (yield) - 1
        score[who_scored] = score[who_scored] + 1
