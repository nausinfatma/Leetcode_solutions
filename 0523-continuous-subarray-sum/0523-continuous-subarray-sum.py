class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        prefix_sum = 0
        remainder_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False