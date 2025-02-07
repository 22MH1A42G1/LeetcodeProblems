from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        c=defaultdict(int)
        b=defaultdict(int)
        ans=[]
        for i,j in queries:
            if i in b:
                c[b[i]]-=1
                if c[b[i]]==0:
                    del c[b[i]]
                b[i] = j
                c[j] += 1
            else:
                c[j]+=1
                b[i]=j
            ans.append(len(c.keys()))
        return ans