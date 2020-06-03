" Student Attendance Record I "

class Solution:
    def checkRecord(self, s: str) -> bool:
        cnta,flag=0,0
        for i in range(len(s)):
            if s[i]=='A':
                cnta+=1
                flag=0
            elif s[i]=='P':
                flag=0
            elif s[i]=='L' and flag <2:
                flag+=1
            elif s[i]=='L' and flag>=2:
                return False
        if cnta >1:
            return False
        return True


sol=Solution()
print (sol.checkRecord("PPALLPA"))
