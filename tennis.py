from coroutine import coroutine


def point_name(point):
    return ["0", "15", "30", "40"][point]


def round_score(score):
    return "(" + str(score[0]) + ":" + str(score[1]) + ")"


def simple_score(score, overall_score):
    return point_name(score[0]) + "-" + point_name(score[1]) + " " + round_score(overall_score)


def deuce_score(score, overall_score):
    if score[0] == score[1]:
        return "deuce " + round_score(overall_score)
    else:
        if score[0] > score[1]:
            return "advantage player 1 " + round_score(overall_score)
        else:
            return "advantage player 2 " + round_score(overall_score)


def won_score(score, overall_score):
    if score[0] > score[1]:
        return "player 1 won " + round_score(overall_score)
    else:
        return "player 2 won " + round_score(overall_score)


@coroutine
def game(scoreboard):
    overall_score = [0, 0]
    while True:
        sentence_score = [0, 0]

        scoreboard(simple_score(sentence_score, overall_score))

        while True:
            scorer = yield from get_scorer()
            increase_score(sentence_score, scorer)

            if sentence_won(sentence_score):
                scoreboard(won_score(sentence_score, overall_score))
                increase_score(overall_score, scorer)
                break
            elif in_deuce(sentence_score):
                scoreboard(deuce_score(sentence_score, overall_score))
            else:
                scoreboard(simple_score(sentence_score, overall_score))


def increase_score(score, who_scored):
    score[who_scored] = score[who_scored] + 1


def get_scorer():
    return (yield) - 1


def in_deuce(score):
    return score[0] >= 3 and score[1] >= 3


def sentence_won(score):
    return (score[0] > 3 or score[1] > 3) and abs(score[0] - score[1]) > 1
