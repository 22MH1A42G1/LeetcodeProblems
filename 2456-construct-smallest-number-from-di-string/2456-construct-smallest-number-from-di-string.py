class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = "" 
        l1 = [] 
        for i, j in enumerate(pattern + "I", start = 1): 
            l1.append(str(i))  
            while l1 and j == "I":
                res += l1.pop() 
        return res