" Find and Replace Pattern "


class Solution:
    def findAndReplacePattern(self, words, pattern):
        res = []
        for word in words:
            dic = {}
            i, j, flag = 0, len(word), 1
            while i < j:
                if pattern[i] in dic:
                    if dic[pattern[i]] != word[i]:
                        flag = 0
                        break
                else:
                    if word[i] not in dic.values():
                        dic[pattern[i]] = word[i]
                    else:
                        flag = 0
                        break
                i += 1
            if flag:
                res.append(word)

        return res

sol=Solution()
print (sol.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb" ))
