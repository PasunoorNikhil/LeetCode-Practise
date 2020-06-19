" Assign Cookies "

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_idx,c_idx=0,0
        ans=0
        while g_idx<len(g) and c_idx<len(s):
            if g[g_idx]<=s[c_idx]:
                ans+=1
                g_idx+=1
                c_idx+=1
            else:
                c_idx+=1
            
        return ans
