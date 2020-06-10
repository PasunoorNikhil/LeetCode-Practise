" Check If All 1's Are at Least Length K Places Away "

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flag=True
        for i in range(len(nums)):
            if flag and nums[i]==1:
                lastpos=i
                flag=False
            elif not flag and nums[i]==1:
                if i-lastpos-1>=k:
                    lastpos=i
                    
                else:
                    return False
        return True
