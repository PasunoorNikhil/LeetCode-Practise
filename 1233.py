"  Remove Sub-Folders from the Filesystem "

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root_set=set()
        folder.sort(key=lambda x:(len,x))
        for i in range(len(folder)):
            current=folder[i]
            tmp,flag="",True
            for j in range(len(current)):
                if current[j]=="/" and flag:
                    flag=False
                elif current[j]=="/" and not flag:
                    if tmp in root_set:
                        break
                elif j==len(current)-1:
                    root_set.add(current)
                tmp+=current[j]

        return list(root_set)
                
        
                        
        
