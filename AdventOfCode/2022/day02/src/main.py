if __name__ == "__main__":
    arr = [1, 2, 3]

    def point_to_win(p1):
        return (p1 % 3) + 1

    def point_to_lose(p1):
        return arr[(p1 + 1) % 3]

    print("wins", point_to_win(3))
    print("lose", point_to_lose(3))

    rock, paper, scisor = 1, 2, 3
    term_scores = {
        "A": rock,
        "B": paper,
        "C": scisor,
    }

    # scisor defetas paper
    # paper defetas rock
    # rock defetas scisor

    win, lose, draw = 6, 0, 3

    p2_score = 0

    with open("input2.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            p1, p2 = line.split()

            if p2 == "X":
                p2_score += lose
                p2 = point_to_lose(term_scores[p1])
            elif p2 == "Y":
                p2_score += draw
                p2 = term_scores[p1]
            elif p2 == "Z":
                p2_score += win
                p2 = point_to_win(term_scores[p1])
            p2_score += p2
        print(p2_score)
