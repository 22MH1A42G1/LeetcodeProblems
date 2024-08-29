class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = height[0] # knowing absolute max for both sides is not necessary, as
        r_max = height[-1] #  .. as only the lower value matters
        n = len(height)
        left = 1
        right = n-2

        if n <= 2:
            return 0

        water = 0
        while left <= right:
            # pick whatever side is lesser, so you know the min() will save you
            if l_max <= r_max:
                # consider adding water from height[left]
                water += max(0, min(l_max, r_max) - height[left])
                l_max = max(l_max, height[left])
                left += 1
            else:
                # consider adding water from height[right]
                water += max(0, min(l_max, r_max) - height[right])
                r_max = max(r_max, height[right])
                right -= 1
                
        return water