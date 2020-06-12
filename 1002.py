" Find Common Characters "

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dic=collections.Counter(A[0])
        res=[]
        for i in range(1,len(A)):
            dic2=collections.Counter(A[i])
            for key in dic:
                if key not in dic2:
                    dic2[key]=0
                dic[key]=min(dic[key],dic2[key])
              
        
        for key,value in dic.items():
            if value>0:
                res.extend([key]*value)
        return res
