" Least Number of Unique Integers after K Removals "

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic=collections.Counter(arr)
        res=list(dic.values())
        res.sort()
        i=0
        ans=k
        for x in res:
            ans=ans-x
            if ans==0:
                return len(res)-i-1
            elif ans<0:
                return len(res)-i
            i+=1
            
            
            
