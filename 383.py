" Ransom Note "

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1=collections.Counter(ransomNote)
        dic2=collections.Counter(magazine)
        for key,value in dic1.items():
            if key not in dic2 :
                return False
            elif dic1[key]>dic2[key]:
                return False
        return True
