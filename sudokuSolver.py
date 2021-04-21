import sys
import UserInfo
import BoardInfo
import solvingAlgorithm


def getUserInfo():
    username = input("Hello, Please enter your username: ")
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    sudokuUser = UserInfo.User(fName, lName, username)
    return sudokuUser

def printPuzzle(board):
    print("")
    for row in board:
        for column in row:
            print(column, end="")
        print("")
    print("\n")


def getPuzzle(user):
    fileName = input("Enter the name of a file containing a puzzle: \n")
    fileName = str(fileName)
    sudokuTable = []
    puzzleFile = open(fileName, "r")
    for x in puzzleFile:
        row = []
        for y in x:
            if(y != '\n'):
                row.append(int(y))
        sudokuTable.append(row)
        row = []
        # print(x, end="")
    # print(sudokuTable, end="")
    sudoku_board = BoardInfo.Board(sudokuTable, [], user)
    return sudoku_board


def main():
    print("This is the main function")
    user = getUserInfo()
    puzzle = getPuzzle(user)

    # print("Hello! your name is: {} {} and your username is: {}".format(user.fName, user.lName, user.username))
    print("This is the unsolved puzzle")
    printPuzzle(puzzle.unsolved)
    solvingAlgorithm.solveSudoku(puzzle.unsolved, 0, 0)
    printPuzzle(puzzle.unsolved)
    
    print("\n")


# def test():
#     user = getUserInfo()
#     puzzle = getPuzzle(user)
#     printPuzzle(puzzle.unsolved)





# test()
main()
