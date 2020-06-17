" Replace Elements with Greatest Element on Right Side "

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp=[0]*len(arr)
        tmp[-1]=-1
        maximum=float('-inf')
        res=[]
        for i in range(len(arr)-1,-1,-1):
            maximum=max(arr[i],maximum)
            tmp[i]=maximum
        for i in range(len(arr)-1):
            res.append(tmp[i+1])
        res.append(-1)
        return res
            
