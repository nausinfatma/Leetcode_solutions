import random
import bisect

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix = []
        total = 0

        for a, b, x, y in rects:
            
            total += (x - a + 1) * (y - b + 1)
            self.prefix.append(total)

    def pick(self) -> list[int]:
        
        target = random.randint(1, self.prefix[-1])

        
        i = bisect.bisect_left(self.prefix, target)

        a, b, x, y = self.rects[i]

        
        u = random.randint(a, x)
        v = random.randint(b, y)

        return [u, v]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()