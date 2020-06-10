" Partition Labels "

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos,res={},[]
        for i,char in enumerate(S):
            pos[char]=i
        start,end,prev=0,0,0
        while start<len(S):
            char=S[start]
            end=max(end,pos[char])
            if start==end:
                res.append(start+1-prev)
                prev = start+1
            start+=1
        return res
            
