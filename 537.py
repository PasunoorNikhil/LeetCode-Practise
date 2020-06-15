" Complex Number Multiplication "

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def process(string):
            s=string.split('+')
            x=int(s[0])
            y=int(s[1][:-1])
            return[x,y]
        A=process(a)
        B=process(b)
        i=A[0]*B[0]+A[1]*B[1]*-1
        j=A[1]*B[0]+A[0]*B[1]
        return str(i)+"+"+str(j)+"i"
