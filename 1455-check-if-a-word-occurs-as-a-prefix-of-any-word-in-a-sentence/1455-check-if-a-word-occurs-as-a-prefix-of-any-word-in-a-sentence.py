class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,j in enumerate(sentence.split(' '), 1):
            if j.startswith(searchWord):
                return i
        return -1