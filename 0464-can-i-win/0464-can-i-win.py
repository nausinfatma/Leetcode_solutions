class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        memo = {}

        def solve(used, remaining):
            if used in memo:
                return memo[used]

            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << (num - 1)

                if used & bit:
                    continue

                if num >= remaining or not solve(used | bit, remaining - num):
                    memo[used] = True
                    return True

            memo[used] = False
            return False

        return solve(0, desiredTotal)
