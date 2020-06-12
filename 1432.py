" Max Difference You Can Get From Changing an Integer "

class Solution:
    def maxDiff(self, num: int) -> int:
        a=b=str(num)
        
        for char in a:
            if char!="9":
                a=a.replace(char,"9")
                break
        if b[0]!="1":
            b=b.replace(b[0],"1")
        else:
            for i in range(1,len(b)):
                if  b[i] not in"01":
                    b=b.replace(b[i],"0")
                    break
        return int(a)-int(b)
            
