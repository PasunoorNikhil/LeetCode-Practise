" Count Largest Group "

class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic={}
        ans=0
        for num in range(1,n+1):
            res=list((str(num)))
            key=0
            for i in res:
                key+=int(i)
            if key in dic:
                dic[key]+=1
            else :
                dic[key]=1
        max_group=max(dic.values())
        for value in dic.values():
            if value==max_group:
                ans+=1

        return ans
