" Custom Sort String "

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic,res={},""
        for x in T:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        for y in S:
            if y in dic:
                for z in range(dic[y]):
                    res+=y
                dic.pop(y)
        for key,value in dic.items():
            for i in range(value):
                res+=key
                
        return res
        
