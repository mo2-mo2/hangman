def hungman(word):
    wrong=0
    stages=["",
            "________    ",
            "|       |   ",
            "|       O   ",
            "|      /|\  ",
            "|      / \  ",
            "|           "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to hungman game")
    while wrong<len(stages)-1:
        print("\n")
        msg="Guess a letter:"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("YOU WIN")
            print("".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("YOU LOSE")
        print("Answer is {}".format(word))

hungman("cat")
