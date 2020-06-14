" Distant Barcodes "

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dic=collections.Counter(barcodes)
        i=0
        res=[0]*len(barcodes)
        for key,value in dic.most_common():
            for x in range(value):
                res[i]=key
                i+=2
                if i>=len(barcodes):
                    i=1
        return res
