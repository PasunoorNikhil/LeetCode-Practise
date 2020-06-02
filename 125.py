"Valid Palindrome"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        s=s.lower()
        while i < j :
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
        return True
sol=Solution()
print (sol.isPalindrome("A man, a plan, a canal: Panama"))
