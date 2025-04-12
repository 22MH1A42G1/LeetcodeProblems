class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1: return 9//k
        k_pals, ans = set(), 0
        pals_left = product(*[digits[1:]]+[digits] *((n-1)//2)) 
        for pal_left in pals_left:
            pal_rght = pal_left[::-1][n%2:]        
            pal = ''.join(((*pal_left, *pal_rght)))
            if int(pal)%k == 0:                 
                k_pals.add(''.join(sorted(pal)))
        for k_pal in k_pals:
            ctr = Counter(k_pal)                          
            denom = reduce(mul, map(factorial, ctr.values()))
            ans+= factorial(n)*(n - ctr['0'])//(denom * n)
        return ans