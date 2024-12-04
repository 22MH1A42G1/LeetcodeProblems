class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n=len(spaces), len(s)
        spaces.append(n)
        t=[' ']*(m+n)
        i, j=0, 0
        while i<n:
            while i<n and i!=spaces[j]:
                t[i+j]=s[i]
                i+=1
            if j<m:
                t[i+j+1]=s[i]
                j+=1
            i+=1
        return "".join(t)