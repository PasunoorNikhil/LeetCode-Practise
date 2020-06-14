" Check If Word Is Valid After Substitutions "

class Solution:
    def isValid(self, S: str) -> bool:
        stack=[]
        i,j=0,len(S)
        while i <j:
            if S[i]=="c" and len(stack)>=2:
                if stack[-1]=="b" and stack[-2]=="a":
                    stack.pop()
                    stack.pop()
            else:
                stack.append(S[i])
            i+=1
        if len(stack)==0:
            return True
        return False
            
        
