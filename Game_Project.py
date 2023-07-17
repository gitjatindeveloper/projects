# game of tic tac toe manually for two players
def sum(a, b, c):
    return a + b + c

def getBoard(xplay, yplay):
    # function for implement of X and O
    # turnary operator - 1 if 1 else 0 - 1
    zero = 'X' if xplay[0] else ('O' if yplay[0] else 0)
    one = 'X' if xplay[1] else ('O' if yplay[1] else 1)
    two = 'X' if xplay[2] else ('O' if yplay[2] else 2)
    three = 'X' if xplay[3] else ('O' if yplay[3] else 3)
    four = 'X' if xplay[4] else ('O' if yplay[4] else 4)
    five = 'X' if xplay[5] else ('O' if yplay[5] else 5)
    six = 'X' if xplay[6] else ('O' if yplay[6] else 6)
    seven = 'X' if xplay[7] else ('O' if yplay[7] else 7)
    eight = 'X' if xplay[8] else ('O' if yplay[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xplay, yplay):
    # function for check lose or win 
    Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8,], [0, 4, 8], [2, 4, 6]]
    for win in Wins:
        if(sum(xplay [win[0]], xplay [win[1]], xplay [win[2]]) == 3):
            print("X win the match")
            return 1
        if(sum(yplay [win[0]], yplay [win[1]], yplay [win[2]]) == 3):
            print("O win the match")
            return 0
    return -1    

# main code
if __name__ == "__main__":
    xplay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yplay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for o
    print("Welcome to Tic Tac Toe game")
    while(True):
        getBoard(xplay, yplay)
        if (turn == 1):
            value = int(input("x's chance! \nenter your choice : "))
            xplay[value] = 1
        else:
            value = int(input("O's chance! \nenter your choice : "))
            yplay[value] = 1
        cwin = checkWin(xplay, yplay)
        if(cwin != -1):
            print("Match over")
            break
        turn = 1 - turn   