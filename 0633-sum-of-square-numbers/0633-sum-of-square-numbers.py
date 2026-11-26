import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for x in range(int(math.sqrt(c)) + 1):
            y = c - x*x

            y = math.sqrt(y)

            if y.is_integer():

                return True

        return False