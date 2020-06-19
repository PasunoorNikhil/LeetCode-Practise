" Top K Frequent Words "

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=[]
        dic=collections.Counter(words)
        for key,value in dic.items():
            res.append(key)
        res.sort(key=lambda x:(-dic[x],x))
        return res[:k]
        
