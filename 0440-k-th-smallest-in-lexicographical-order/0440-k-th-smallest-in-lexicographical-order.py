class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # A helper function to count how many numbers lie between the prefix `curr`
        # and the next prefix (`curr + 1`), within the range [1, n].
        def count_steps(curr, n):
            steps = 0
            first = curr
            next_prefix = curr + 1
            while first <= n:
                # Count the numbers between `first` and `min(n + 1, next_prefix)`
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10
            return steps
        
        curr = 1  # Start with the first prefix, "1"
        k -= 1    # Decrease k by 1 because we consider `1` as the first number.
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # If the k-th number is not in the current subtree, move to the next sibling.
                k -= steps
                curr += 1
            else:
                # If the k-th number is in the current subtree, go deeper into the subtree.
                curr *= 10
                k -= 1
        
        return curr