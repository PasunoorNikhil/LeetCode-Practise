" Sort Characters By Frequency "

import collections
class Solution:
    def frequencySort(self, s) :
        res=""
        dic=collections.Counter(s)
        for k,v in dic.most_common():
            for x in range(v):
                res+=k
        return res


sol=Solution()
print (sol.frequencySort("cncaa"))
