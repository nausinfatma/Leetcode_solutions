from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for x in nums:
            d[x] += 1

        for x in d:
            if d[x] > 1:
                return x