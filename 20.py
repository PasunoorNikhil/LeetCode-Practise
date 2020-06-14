" Valid Parentheses "

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i,j=0,len(s)
        while i<j:
            if len(stack)== 0 and s[i] in ")]}" : 
                    return False
            if s[i]==")" and stack[-1]=="(":
                stack.pop()
            elif s[i]=="]" and stack[-1]=="[":
                stack.pop()
            elif s[i]=="}" and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        if len(stack)==0:
            return True
        return False
            
