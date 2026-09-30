class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for bit in range(30, -1, -1):
            mask |= (1 << bit)

            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            candidate = ans | (1 << bit)

            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    ans = candidate
                    break

        return ans