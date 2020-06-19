" Longest Harmonious Subsequence "

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_len=0
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for j in dic:
            if  j+1 in dic:
                max_len=max(max_len,dic[j]+dic[j+1])
        return max_len
        
