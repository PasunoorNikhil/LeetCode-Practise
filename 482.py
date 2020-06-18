" License Key Formatting "

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        tmp = ""
        res = ""
        flag = True
        for char in S.upper():
            if char.isalnum():
                tmp += char
        num_dashes, fgrp_len = divmod(len(tmp), K)
        if K>=len(tmp):
            return tmp
        if fgrp_len==0:
            num_dashes-=1
        i, j = 0, len(tmp)
        while i <=j - K:
            if flag and fgrp_len != 0:
                res += tmp[0:fgrp_len]
                i = fgrp_len
                flag=False
            else:
                res += tmp[i:i + K]
                i = i + K
            if num_dashes > 0:
                res += "-"
            num_dashes -= 1
        return res
        
