def isValidSudoku(board):
        def isValid(listRange, checkList=list(range(1,10))):
            for eachDigit in listRange:
                if eachDigit.isnumeric():
                    # for duplicate numbers return False
                    # print(f"Digit {eachDigit} Checklist {checkList}")
                    if int(eachDigit) not in checkList:
                        return False
                    else:
                        checkList.remove(int(eachDigit))
            return True
        # row check
        for eachRow in board:
            if not(isValid(eachRow,list(range(1,10)))):
                # print(f"Row: {eachRow}")
                return False
        # column check
        for i in range(0,9):
            if not(isValid([val[i] for val in board],list(range(1,10)))):
                # print(f"Col: {i}")
                return False
        # 3x3 grid check
        for i in range(0,9,3):
            for j in range(0,9,3):
                t = [val[j:j+3] for val in board[i:i+3]]
                flat_list = [item for sublist in t for item in sublist]
                if not(isValid(flat_list,list(range(1,10)))):
                    # print(f"Grid: {i}{j}")
                    return False
        return True




board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
print("#*80")

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))