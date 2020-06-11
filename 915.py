" Partition Array into Disjoint Intervals "

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left,right=[0]*len(A),[0]*len(A)
        left[0]=A[0]
        right[-1]=A[-1]
        for i in range(1,len(A)):
            tmp=max(A[i],left[i-1])
            left[i]=tmp
        for j in range(len(A)-2,-1,-1):
            tmp=min(A[j],right[j+1])
            right[j]=tmp
            
        for k in range(1,len(A)):
            if left[k-1]<=right[k]:
                return k
        
