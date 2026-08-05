class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        m = n//2
        a = sum(1 for i in s[:m] if i.lower() in "aeiou")
        b = sum(1 for i in s[m:] if i.lower() in "aeiou")
        print(a,b)
        return a==b