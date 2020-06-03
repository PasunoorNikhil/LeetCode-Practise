" Contains Duplicate II "


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for idx,x in enumerate(nums):
            if x in dic and idx-dic[x]<=k :
                return True
            dic[x]=idx
        return False

