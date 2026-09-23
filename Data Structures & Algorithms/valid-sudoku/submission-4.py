class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force approach
        # Brute force should be first to satisfy the first condition which is see that
        # We can use
        for row in range(9): # Checking if the rows are valid or not
            seen = set()
            for i in range(9):       
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        
        for col in range(9): # if the columns are valid or not
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                else:
                    seen.add(board[i][col])
        for sqr in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sqr//3) * 3 + i # let's say sqr is 1 then 1//3 = 0 *3 =0 so starting index becomes zero here in the box and then + 0 which is first and +1 second and so on. 
                    col = (sqr%3) *3 + j # this gives the reminder so we can track left middle and right column of the each square, 0,3,6 left and 1,4,7 middle and 2,5,8 right 
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True
