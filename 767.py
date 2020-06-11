"  Reorganize String "

class Solution:
    def reorganizeString(self, S: str) -> str:
        dic=collections.Counter(S)
        res=[""]*len(S)
        i=0
        for key,value in dic.most_common():
            if value>(len(S)+1)/2:
                return ""
            for k in range(value):
                if i>=len(S):
                    i=1
                    res[i]+=key
                else:
                    res[i]+=key
                i+=2
        return "".join(res)
                    
        
