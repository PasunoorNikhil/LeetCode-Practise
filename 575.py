" Distribute Candies "

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        ans=0
        dic=collections.Counter(candies)
        for key in dic:
            ans+=1
            if ans >=len(candies)/2:
                return ans
        return ans
            
        
