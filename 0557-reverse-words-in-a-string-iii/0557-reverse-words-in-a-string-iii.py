class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        l = []
        for i in w:
            l.append(i[::-1])
        ans = ' '.join(map(str,l))
        print(ans)
        return ans