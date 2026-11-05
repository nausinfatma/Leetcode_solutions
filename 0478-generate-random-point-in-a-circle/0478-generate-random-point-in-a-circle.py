import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> list[float]:
        theta = random.uniform(0, 2 * math.pi)
        d = self.r * math.sqrt(random.random())

        x = self.xc + d * math.cos(theta)
        y = self.yc + d * math.sin(theta)

        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()