" Group Anagrams "


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            key=str(sorted(word))
            if key in dic:
                dic[key].append(word)
            else:
                dic[key]=[word]
        return list(dic.values())
        
