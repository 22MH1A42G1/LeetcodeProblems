class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        z=0
        st = []
        for i in nums:
            z+=i
            st.append(z)
        print(st)
        return st.count(0)