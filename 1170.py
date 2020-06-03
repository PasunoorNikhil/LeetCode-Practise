" Compare Strings by Frequency of the Smallest Character "

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res,wordstmp=[],[]
        for y in words:
            wordstmp.append(self.frequncyofsmallest(y))
    
        for i in range(len(queries)):
            tmp=self.frequncyofsmallest(queries[i])
            count=0
            for z in wordstmp:
                if tmp<z:
                    count+=1
            res.append(count)
        return res
    
    
    def frequncyofsmallest(self,string):
        smallchr=min(string)
        smallchrcnt=0
        for x in string:
            if x==smallchr:
                smallchrcnt+=1
        return smallchrcnt
        
