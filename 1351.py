" Count Negative Numbers in a Sorted Matrix "

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in reversed(i):
                if j<0:
                    count+=1
                else:
                    break
        return count
                
