" Divide Array in Sets of K Consecutive Numbers "

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dic=collections.Counter(nums)
        for num in sorted(nums):
            if num in dic:
                for y in range(num,num+k):
                    if y in dic:
                        dic[y]-=1
                        if dic[y]==0:
                            del dic[y]
                    else:
                        return False
        return True
        
