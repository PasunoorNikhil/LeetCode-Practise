class Solution:
    def generateTheString(self, n: int) -> str:
        a='x'
        b='y'
        res=''
        if n%2!=0:
            for x in range(n):
                res+=a
        else:
            for x in range(n-1):
                res+=a
            res+=b
        return res
