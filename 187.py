" Repeated DNA Sequences "


class Solution:
    def findRepeatedDnaSequences(self, s) :
        dic={}
        seen=set()
        for i in range(len(s)-9):
            sequence=s[i:i+10]
            if sequence in dic:
                seen.add(sequence)
            else:
                dic[sequence]=1
        return list(seen)

