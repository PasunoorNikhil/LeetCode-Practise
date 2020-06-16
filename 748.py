" Shortest Completing Word "

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = ""
        min_len = 30
        ans = None
        for char in licensePlate.lower():
            if char.isalpha():
                lp += char
        dic = collections.Counter(lp)
        for word in words:
            tmp = collections.Counter(word)
            fl = True
            for key, value in dic.items():
                if key in tmp and dic[key] <= tmp[key]:
                    continue
                else:
                    fl = False
                    break
            if fl and not ans:
                ans = word
            if fl and len(word) < len(ans):
                ans = word
                
        return ans
                    
            
