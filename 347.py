" Top K Frequent Elements "

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        values = heapq.nlargest(k, dic, key=dic.get)
        return values
