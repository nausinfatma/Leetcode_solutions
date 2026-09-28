from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        d = defaultdict(list)

        for i in range(len(equations)):
            d[equations[i][0]] += [(equations[i][1], values[i])]
            d[equations[i][1]] += [(equations[i][0], 1 / values[i])]

        ans = []

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for x, y in d[curr]:

                if x not in visited:
                    result = dfs(x, target, visited)

                    if result != -1.0:
                        return y * result

            return -1.0

        for start, end in queries:

            if start not in d or end not in d:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set()))

        return ans
