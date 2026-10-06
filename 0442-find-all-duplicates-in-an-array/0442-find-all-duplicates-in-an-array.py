class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        arr = []

        for x in nums:
            x = abs(x)

            if nums[x - 1] < 0:
                arr.append(x)
            else:
                nums[x - 1] = -nums[x - 1]

        return arr