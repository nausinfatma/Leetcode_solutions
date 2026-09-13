from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = defaultdict(int)

        for x in nums:
            d[x] += 1

        sorted_dict = sorted(d.items(), key= lambda x: x[1], reverse = True)

        new = []
        for i in range(k):
            new.append(sorted_dict[i][0])

        return new
