class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(board):
            for row in board:
                s = set()
                for d in row:
                    if d not in "123456789." or d in s:
                        return False
                    if d != ".":
                        s.add(d)

            return True

        def check_column(board):
            for i in range(0, 9):
                s = set()
                for row in board:
                    if row[i] in s or row[i] not in "123456789.":
                        return False
                    if row[i] != ".":
                        s.add(row[i])
            return True

        def check_square(board):
            for i in range(0, 6, 3):
                start1 = i
                for i in range(0, 6, 3):
                    start2 = i
                    s = set()
                    for i1 in range(start1, start1 + 3):
                        for i2 in range(start2, start2 + 3):
                            d = board[i1][i2]
                            print(d)
                            if d not in "123456789.":
                                return False
                            if d in s:
                                return False
                            if d != ".":
                                s.add(d)
                                print(s)
            return True
        return check_square(board) and check_row(board) and check_column(board)

                
                    
                
                

                