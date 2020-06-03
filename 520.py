"Detect Capital"
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt=0
        for i in range(len(word)):
            if word[i].isupper() and cnt==i:
                cnt+=1
                continue
            elif word[i].islower() and cnt<2 :
                continue
            else:
                return False
        return True




sol=Solution()
print (sol.detectCapitalUse("LeetcodE"))
