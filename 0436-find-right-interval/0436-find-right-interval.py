class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))

        ans = []

        for start, end in intervals:
            left = 0
            right = len(starts) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    result = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

            ans.append(result)

        return ans