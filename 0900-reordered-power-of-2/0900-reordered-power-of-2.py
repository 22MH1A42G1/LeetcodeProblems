class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            # Counts the frequency of each digit in a number
            counts = [0] * 10
            if num == 0:  # Handle the case of 0 specifically if it could be an input (though constraints say n >= 1)
                counts[0] = 1
                return tuple(counts)
            
            while num > 0:
                counts[num % 10] += 1
                num //= 10
            return tuple(counts)

        n_counts = count_digits(n)

        # Iterate through powers of 2
        # 2^0 = 1, up to 2^29 (since 2^30 > 10^9)
        for i in range(30): 
            power_of_two = 1 << i  # This is equivalent to 2**i
            if count_digits(power_of_two) == n_counts:
                return True
        
        return False