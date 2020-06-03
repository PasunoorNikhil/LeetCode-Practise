" Buddy Strings "

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A == B and len(set(A)) < len(A): return True
        tmp=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                tmp.append(A[i])
                tmp.append(B[i])
        if len(tmp)==4 and tmp[0]==tmp[3] and tmp[1]==tmp[2]:
            return True
        return False
