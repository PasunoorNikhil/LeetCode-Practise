class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic={}
        for x in J:
            if dic.get(x,0)==0:
                dic[x]=1
        count=0
        for y in S:
            if dic.get(y,0)==1:
                count+=1
        return count
