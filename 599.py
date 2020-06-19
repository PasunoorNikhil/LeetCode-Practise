" Minimum Index Sum of Two Lists "

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic,res={},[]
        mini=float('inf')
        for i in range(len(list1)):
            restaurant1=list1[i]
            dic[restaurant1]=i
        for j in range(len(list2)):
            restaurant2=list2[j]
            if restaurant2 in dic:
                min_idx=dic[restaurant2]+j
                if min_idx< mini:
                    res=[]
                    mini=min_idx
                    res.append(restaurant2)
                elif min_idx==mini:
                    res.append(restaurant2)
        return res
