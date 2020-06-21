" Lemonade Change "

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5,cnt_10=0,0
        for bill in bills:
            if bill==5:
                cnt_5+=1
            elif bill==10:
                if cnt_5>0:
                    cnt_5-=1
                else:
                    return False
                cnt_10+=1
            elif bill==20:
                if cnt_10>0 and cnt_5>0:
                    cnt_10-=1
                    cnt_5-=1
                elif cnt_5>=3:
                    cnt_5-=3
                else:
                    return False
        return True
