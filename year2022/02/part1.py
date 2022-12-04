def decide_val():
    if me == "X":
        return 1
    elif me == "Y":
        return 2
    else:
        return 3


with open("input.txt") as file:
    scores = 0
    for line in file:
        line = line.strip("\n")
        opponent, me = line.split(" ")
        if (
            (me == "Y" and opponent == "A")
            or (me == "Z" and opponent == "B")
            or (me == "X" and opponent == "C")
        ):
            score = decide_val() + 6
            scores += score
        elif (
            (opponent == "A" and me == "X")
            or (opponent == "B" and me == "Y")
            or (opponent == "C" and me == "Z")
        ):
            score = decide_val() + 3
            scores += score
        else:
            score = decide_val() + 0
            scores += score
    print(scores)
