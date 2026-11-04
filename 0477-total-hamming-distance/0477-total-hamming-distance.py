class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(32):
            ones = 0

            for num in nums:
                if num & (1 << i):
                    ones += 1

            zeros = n - ones
            ans += ones * zeros

        return ans