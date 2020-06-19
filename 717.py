" 1-bit and 2-bit Characters "

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx=0
        i,j=0,len(bits)
        while i<j:
            if bits[i]==1:
                i+=2
            else:
                if i==j-1:
                    return True
                i+=1
        return False
