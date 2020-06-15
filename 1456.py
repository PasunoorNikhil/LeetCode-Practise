" Maximum Number of Vowels in a Substring of Given Length "

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        window=s[0:k]
        cnt=0
        for char in window:
            if char in vowels:
                cnt+=1
        max_cnt=cnt
        for i in range(k,len(s)):
            cur_char=s[i]
            pre_char=s[i-k]
            if cur_char in vowels:
                cnt+=1
            if pre_char in vowels:
                cnt-=1
            max_cnt=max(cnt,max_cnt)
        return max_cnt
