" Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold "

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        res=0
        j = k - 1
        cursum = sum(arr[:k - 1])
        while j < len(arr):
            cursum += arr[j]
            avg = cursum / k
            if avg >= threshold:
                res += 1
            cursum -= arr[i]
            i += 1
            j += 1
        return res
        
