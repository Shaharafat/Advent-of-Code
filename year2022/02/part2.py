def make_win(op):
    if op == "A":
        return 2 + 6
    elif op == "B":
        return 3 + 6
    else:
        return 1 + 6


def make_draw(op):
    if op == "A":
        return 1 + 3
    elif op == "B":
        return 2 + 3
    else:
        return 3 + 3


def make_lose(op):
    if op == "A":
        return 3 + 0
    elif op == "B":
        return 1 + 0
    else:
        return 2 + 0


with open("input.txt") as file:
    scores = 0
    for line in file:
        line = line.strip("\n")
        opponent, me = line.split(" ")

        if me == "X":
            score = make_lose(opponent)
            scores += score
        elif me == "Y":
            score = make_draw(opponent)
            scores += score
        else:
            score = make_win(opponent)
            scores += score

    print(scores)
