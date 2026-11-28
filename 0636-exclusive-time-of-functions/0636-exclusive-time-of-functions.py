class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            num, com, time = log.split(':')
            num = int(num)
            time = int(time)

            if com == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time

                stack.append(num)
                prev_time = time

            else:  
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res
