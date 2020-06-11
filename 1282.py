" Group the People Given the Group Size They Belong To "

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizedic=collections.defaultdict(list)
        res=[]
        for idx,i in enumerate(groupSizes):
            sizedic[i].append(idx)
        for key,li in sizedic.items():
            for i in range(0,len(li),key):
                res.append(li[i:i+key])
        return res
                
