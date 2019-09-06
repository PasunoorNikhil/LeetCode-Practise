class Solution:
    def validMountainArray(self, A) :
        increasing,decreasing=0,0
        if len(A)<=3:
            return False
        for i in range(1,len(A)):
            if A[i-1]<=A[i] and decreasing==0 :
                if increasing==1:
                    continue
                elif increasing==0:
                    increasing=1
            elif A[i-1]<=A[i] and decreasing!=0:
                return False
            elif A[i-1]>=A[i] and increasing==1:
                if decreasing==1:
                    continue
                elif decreasing==0:
                    decreasing=1
            elif A[i-1]>=A[i] and increasing==0:
                return False
        if increasing==1 and decreasing==1:
            return True
        else:
            return False
s=Solution()
s.validMountainArray([1,3,2])