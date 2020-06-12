" Backspace String Compare "

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stk_t,stk_s=[],[]
        for char in S:
            if len(stk_s)>0 and char=="#":
                stk_s.pop()
            elif char!="#":
                stk_s.append(char)
        for ch in T:
            if len(stk_t)>0 and ch=="#":
                stk_t.pop()
            elif ch!="#":
                stk_t.append(ch)
                
        s="".join(stk_s)
        t="".join(stk_t)
        if s==t:
            return True
        else:
            return False
                
