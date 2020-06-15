" Flip String to Monotone Increasing "

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        l1, r0 = [0] * len(S), [0] * len(S)
        l1_cnt, r0_cnt = 0, 0
        m = 25000
        for i in range(len(r0) - 1, -1, -1):
            r0[i] = r0_cnt
            if S[i] == "0":
                r0_cnt += 1

        for i in range(len(l1)):
            l1[i] = l1_cnt
            if S[i] == "1":
                l1_cnt += 1

        if l1_cnt  == 0 or r0_cnt==0:
            return 0
        for i in range(len(S)):
            m = min(m, l1[i] + r0[i])

        return m
