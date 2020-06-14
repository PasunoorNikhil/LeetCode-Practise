" Find Lucky Integer in an Array "


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic=collections.Counter(arr)
        res=0
        pre_key=0
        flag=False
        for key,value in dic.items():
            if key==value:
                flag=True
                if value>res:
                    res=value
                    pre_key=key
                elif value==res:
                    pre_key=max(pre_key,key)
        if flag:
            return pre_key
        return -1
                    
                    
        
