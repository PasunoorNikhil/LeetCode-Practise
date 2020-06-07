" Valid Anagram "

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic=collections.Counter(s)
        for char in t:
            if char in dic :
                if dic[char]>1:
                    dic[char]-=1
                else:
                    dic.pop(char)
            else:
                return False
        if not dic:
            return True
        else:
            return False
        
        
