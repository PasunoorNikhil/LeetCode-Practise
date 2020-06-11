" Reshape the Matrix "

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        tmp_r,tmp_c  = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if tmp_c  == c:
                    tmp_r += 1
                    tmp_c = 0
                res[tmp_r][tmp_c] = nums[i][j]
                tmp_c+=1
        return res
        
