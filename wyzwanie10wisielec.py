import random
def hangman():
    words = ["pies", "kot", "papuga", "kaczka", "anastazja", "lololowska", "nazar"]
    word = random.choice(words)
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Gra w Wisielca")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij literę: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Wygrałeś!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(word))

hangman()
