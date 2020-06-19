"  Find Duplicate File in System "

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = []
        dic = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for i in range(1, len(data)):
                tmp = data[i].split("(")
                file_name = tmp[0]
                contents = tmp[1]
                path=root+"/"+file_name
                dic[contents].append(path)
        for key,value in dic.items():
            if len(value)>1:
                res.append(value)
        return res
