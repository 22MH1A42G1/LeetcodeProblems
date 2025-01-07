class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len, reverse=True)
        r = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] in words[i]:
                    r.append(words[j])
        return sorted(set(r))