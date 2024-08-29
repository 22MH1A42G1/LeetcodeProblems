class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s=''.join(sorted(list(i)))
            if s not in d:
                d[s]=[i]
            else:
                d[s].append(i)
        res=[]
        for j in d.values():
            res.append(j)
        return res