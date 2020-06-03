" Squares of a Sorted Array "
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result=[]
        for x in A:
            z=x*x
            result.append(z)
        result.sort()
        return result
