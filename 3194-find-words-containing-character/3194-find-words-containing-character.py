class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i,w in enumerate(words):
            if x in w:
                ans.append(i)
        return ans
