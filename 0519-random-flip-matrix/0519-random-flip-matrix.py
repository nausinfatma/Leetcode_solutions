class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.mapping = {}

    def flip(self) -> list[int]:

        r = random.randrange(self.remaining)
        self.remaining -= 1


        x = self.mapping.get(r, r)
        last = self.mapping.get(self.remaining, self.remaining)


        self.mapping[r] = last


        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.remaining = self.total
        self.mapping.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()