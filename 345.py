"Reverse Vowels of a string"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        res = list(s)
        while i < j:
            if res[i] not in vowels:
                i += 1
            if res[j] not in vowels:
                j -= 1
            if res[i] in vowels and res[j] in vowels:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return "".join(res)


sol=Solution()
print (sol.reverseVowels("hello"))
