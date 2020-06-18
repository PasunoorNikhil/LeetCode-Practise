" The K Weakest Rows in a Matrix "

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarysearch(row):
            lo, hi = 0, len(row)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if row[mid]==1:
                    lo=mid+1
                else:
                    hi=mid
            return lo

        tmp, res = [], []
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            solders = binarysearch(mat[i])
            tmp.append([solders, i])

        tmp.sort(key=lambda x: (x[0], x[1]))
        print(tmp)
        for x in range(k):
            res.append(tmp[x][1])
        return res
