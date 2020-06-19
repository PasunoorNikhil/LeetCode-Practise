" Number of Lines To Write String "

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        cur_width=0
        new_lines=0
        i,j=0,len(S)
        while i <j:
            cur_width+=widths[ord(S[i])-97]
            if cur_width>100:
                cur_width=0
                new_lines+=1
                i-=1
            i+=1
        return [new_lines+1,cur_width]
                
