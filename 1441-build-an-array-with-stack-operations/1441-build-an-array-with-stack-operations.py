class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        t=0
        for i in range(1,n+1):
            ans.append("Push")
            if target[t]==i:
                t+=1
                if t==len(target):
                    break
            else:
                ans.append("Pop")
        return ans