"Reverse Words in a string III"

class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        for idx in range(len(res)):
            word = res[idx]
            i, j = 0, len(word) - 1
            temp = list(word)
            while i < j:
                temp[i], temp[j] = temp[j], temp[i]
                i+=1
                j-=1
            res[idx] = "".join(temp)

        return " ".join(res)


sol=Solution()
print (sol.reverseWords("Let's take LeetCode contest"))
