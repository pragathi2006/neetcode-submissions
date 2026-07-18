class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            d={}
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if board[i][j] not in d:
                        d[board[i][j]]=1
                    else:
                        d[board[i][j]]+=1
            for value in d.values():
                if value>1:
                    return False
        j=0
        while j<len(board[0]):
            d={}
            for i in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] not in d:
                        d[board[i][j]]=1
                    else:
                        d[board[i][j]]+=1
            for value in d.values():
                if value>1:
                    return False
            j+=1
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                d={}
                for l in range(i,i+3):
                    for m in range(j,j+3):
                        if board[l][m]==".":
                            continue
                        if board[l][m] not in d:
                            d[board[l][m]]=1
                        else:
                            return False
        return True                            