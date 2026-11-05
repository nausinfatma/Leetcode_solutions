class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0

        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1
        i = 2
        num = 1

        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)

                if num == 1 and len(s) <= n:
                    count += 1

            num = 3 - num  
            i += 1

        return count
