" Camelcase Matching "

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res=[]
        for word in queries:
            result=self.match(word,pattern)
            res.append(result)
        return res
    
    def match(self,word,pattern):
        i=0
        for c in word:
            if i<len(pattern) and c == pattern[i]:
                i+=1
            elif c.isupper():
                return False            
        if i == len(pattern):
            return True
        else:
            return False
        
       
