"  Majority Element "

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict=dict()
        count=len(nums)/2
        for element in nums:
            if  element not in mydict.keys():
                mydict[element]=1
                
            else:
                mydict[element]+=1
        for key,value in mydict.items():
            if value>count:
                return key
        
