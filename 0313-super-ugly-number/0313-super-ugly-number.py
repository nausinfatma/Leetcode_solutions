class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        dp = [0] * n
        dp[0] = 1

        indexes = [0] * len(primes)

        for i in range(1, n):
            next_number = float("inf")

            for j in range(len(primes)):
                candidate = dp[indexes[j]] * primes[j]

                if candidate < next_number:
                    next_number = candidate

            dp[i] = next_number

            for j in range(len(primes)):
                candidate = dp[indexes[j]] * primes[j]

                if candidate == next_number:
                    indexes[j] += 1

        return dp[n - 1]