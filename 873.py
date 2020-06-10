" Length of Longest Fibonacci Subsequence "

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        ans=0
        numset=set(A)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                x,y=A[i], A[j]
                z=x+y
                cnt=2
                while z in numset:
                    x,y=y,z
                    z=x+y
                    cnt+=1
                    ans=max(cnt,ans)
        return ans if ans>=3 else 0
                    
                    
