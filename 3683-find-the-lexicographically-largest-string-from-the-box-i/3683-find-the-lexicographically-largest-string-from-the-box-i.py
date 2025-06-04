class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word
        ans=""
        for i in range(len(word)):
            ans = max(ans, word[i:min(i+len(word)-numFriends+1, len(word))])
        return ans