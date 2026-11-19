class Solution:
    def arrayNesting(self, nums: list[int]) -> int:

        visited = [False] * len(nums)
        maxm = 0

        for i in range(len(nums)):
            count = 0
            k = i

            while not visited[k]:
                visited[k] = True
                count += 1
                k = nums[k]

            maxm = max(maxm, count)

        return maxm