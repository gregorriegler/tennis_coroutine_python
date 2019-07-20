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

def game():
    score = [0, 0]
    while True:
        print(score_as_string(score))
        whoScored = (yield) - 1
        score[whoScored] = score[whoScored] + 1

g = game()
next(g)
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