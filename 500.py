"  Keyboard Row "

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letters = "qwertyuiopasdfghjklzxcvbnm"
        dic={}
        i = 0
        res=[]
        for k in range(26):
            if k == 10:
                i += 1
            elif k == 19:
                i += 1
            dic[letters[k]] = i
        for word in words:
            flag=True
            i=0
            for char in word.lower():
                if flag:
                    row=dic[char]
                    flag=False
                else:
                    if dic[char]!=row:
                        break
                i+=1
            if i==len(word):
                res.append(word)
        return res
