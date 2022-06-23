def checkNumber(board, num):
    r=False
    for i in range(0,5):
        for j in range(0,5):
            if (board[i][j] == num):
                r=True
                board[i][j]="x"
    return r

def checkRows(board):
    r=False
    for row in board:
        r=True
        for column in row:
            if (column!="x"): r=False
        if (r): break
    return r

def checkColumns(board):
    r=False
    for i in range(0,5):
        r=True
        for j in range(0,5):
            if (board[j][i]!="x"): r=False
        if (r): break
    return r

def winner(board):
    return (checkRows(board) or checkColumns(board))

with open('input.txt','r') as f:
    lines = f.readlines()
    numbers = lines[0]
    boards=[]
    n=2
    while (n<len(lines)-4):
        board=[]
        for i in range(n,n+5):
            line=[]
            for num in lines[i].split():
                line.append(num)
            board.append(line)
        boards.append(board)
        n+=6
    ns=numbers.split(',')
    win=None
    done=0
    all = len(boards)
    for i in range(0,5):
        for b in boards: checkNumber(b,ns[i])
    for i in range(0,len(boards)):
        if (winner(boards[i])):
            win=boards[i]
            boards[i]=None
            done+=1
    n=4
    while (done<all):
        n+=1
        for i in range(0,len(boards)):
            if (boards[i] and checkNumber(boards[i],ns[n]) and winner(boards[i])):
                win=boards[i]
                boards[i]=None
                done+=1

    r=0
    for row in win:
        for column in row:
            if (column!="x"): r+=int(column)
    print(str(r*int(ns[n])))
