class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        req=0
        for i in sentences:
            res=list(map(str,i.split()))
            req=max(req,len(res))
        return req