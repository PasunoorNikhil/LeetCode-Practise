" Reduce Array Size to The Half "

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt,element_cnt,target=0,0,len(arr)/2
        dic=collections.Counter(arr)
        for element, count in dic.most_common(): 
            cnt+=count
            element_cnt+=1
            if cnt>=target:
                return element_cnt
            
