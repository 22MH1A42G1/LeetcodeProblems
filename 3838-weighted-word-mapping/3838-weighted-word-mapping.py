class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=[]
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-ord('a')]
            ans.append(chr(ord('z')-s%26))
        return ''.join(map(str,ans))