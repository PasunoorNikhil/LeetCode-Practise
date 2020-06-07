" Longest Word in Dictionary through Deleting "

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            cnt,i,j=0,0,len(word)-1
            m,n=0,len(s)-1
            while i<=j and m <=n:
                if s[m]==word[i]:
                    i+=1
                    m+=1
                    cnt+=1
                else:
                    m+=1
            if cnt==len(word) :
                return word
        return ""
        
            
            
            
        
                
                
        
