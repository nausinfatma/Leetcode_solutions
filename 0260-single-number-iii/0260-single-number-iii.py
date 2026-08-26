from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        ans = []
        d = defaultdict(int)

        for x in nums:
            d[x] += 1

        for x in d:
            if d[x] == 1:
                ans.append(x)

            if len(ans) == 2:
                return ans