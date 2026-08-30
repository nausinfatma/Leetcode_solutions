class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            left, right = 0, len(sub)

            while left < right:
                mid = (left + right) // 2

                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(sub):
                sub.append(num)
            else:
                sub[left] = num

        return len(sub)