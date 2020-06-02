"Number of segments in a string"
class Solution:
    def countSegments(self, s: str) -> int:
        i,count=1,0
        s=s.strip()
        while i<len(s)-1:
            if s[i]==" " and s[i-1]!=" ":
                count+=1
            i+=1
        if count == 0 and len(s)==0:
            return count
        else:
            return count + 1
sol=Solution()
print (sol.countSegments(" Hello"))
