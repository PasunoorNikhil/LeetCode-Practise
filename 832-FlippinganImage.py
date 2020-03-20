class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for element in A:
            element.reverse()
            for new,x in enumerate(element):
                if x==0:
                    element[new]=1
                if x==1:
                    element[new]=0
        return A 
        
