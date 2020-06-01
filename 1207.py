class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for element in arr:
            if element not in dic:
                dic[element]=1
            else:
                dic[element]+=1
        if len(dic.values())==len(set(dic.values())):
            return True
        return False            
        
