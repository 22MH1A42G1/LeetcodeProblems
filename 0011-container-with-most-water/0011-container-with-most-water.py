class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:

            return 0

        

        # Define left and right pointers, define maximum area

        left = 0

        right = len(height)-1

        max_area = 0

         

        while left < right:

            # Current area is area between left and right pointers

            currentArea = min(height[left], height[right]) * (right - left)

            # Max area is either the max area of the current area

            max_area = max(max_area, currentArea)

            # Condition for moving the pointers

            if height[left] < height[right]:

                left += 1

            else:

                right -= 1

        return max_area