" First Unique Character in a String "

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for x in s:
            if dic.get(x,0)==0:
                dic[x]=1
            else:
                dic[x]+=1
        for idx,ch in enumerate(s):
            if dic[ch]==1:
                return idx
        return -1
            
