" Transpose Matrix "

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows=len(A)
        cols=len(A[0])
        res=[[0 for i in range(rows)] for j in range(cols)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][i]=A[i][j]
                
        return res
