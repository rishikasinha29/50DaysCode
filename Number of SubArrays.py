import math

class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            current_lcm = 1  # Initialize LCM for the current subarray (identity for LCM calculation)
            for j in range(i, n):
                num = nums[j]

                # Optimization 1: If 'k' is not divisible by 'num', then 'k' cannot be the LCM
                # of any subarray containing 'num'. So, we can stop extending this subarray.
                if k % num != 0:
                    break

                # Calculate the LCM of the current subarray ending at 'j'.
                # lcm(a, b) = (a * b) / gcd(a, b)
                current_lcm = (current_lcm * num) // math.gcd(current_lcm, num)

                # Optimization 2: If the current LCM already exceeds 'k', it can never
                # become equal to 'k' by adding more positive numbers.
                if current_lcm > k:
                    break
                
                # If the current LCM is exactly 'k', we found a valid subarray.
                if current_lcm == k:
                    count += 1
        
        return count
