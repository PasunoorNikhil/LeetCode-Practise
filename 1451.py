" Rearrange Words in a Sentence "

class Solution:
    def arrangeWords(self, text: str) -> str:
        text.lower()
        dic=collections.defaultdict(list)
        text+=" "
        s,res="",""
        for char in text:
            if char.isalpha():
                s+=char
            else:
                dic[len(s)].append(s)
                s=""
        tmp=list(dic.keys())
        tmp.sort()
        for key in tmp:
            for value in dic[key]:
                res+=value+" "
        
        return res.capitalize().strip()
        
        
