" Minimum Number of Steps to Make Two Strings Anagram "

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = 0
        dic_s, dic_t = {}, {}
        for x in s:
            if x in dic_s:
                dic_s[x] += 1
            else:
                dic_s[x] = 1
        for y in t:
            if y in dic_t:
                dic_t[y] += 1
            else:
                dic_t[y] = 1
        for key, value in dic_s.items():
            if key not in dic_t:
                cnt += dic_s[key]
            else:
                cnt += dic_s[key] - dic_t[key] if dic_s[key] > dic_t[key] else 0
        return cnt


sol=Solution()
print (sol.minSteps("bab","aba" ))
