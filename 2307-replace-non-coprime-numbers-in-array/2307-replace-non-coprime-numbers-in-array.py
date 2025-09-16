class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st =[]
        for i in nums:
            while st:
                g = gcd(st[-1],i)
                if g==1:
                    break
                i=(st.pop()*i)//g
            st.append(i)
        return st