class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        mi = ''
        for i in letters:
            if i > target:
                mi = i
                break
            else:
                mi = letters[0]
        return mi