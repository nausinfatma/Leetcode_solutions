from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        d = defaultdict(list)

        for x in edges:
            d[x[0]].append(x[1])
            d[x[1]].append(x[0])

        while len(d) > 2:
            leaves = []

            for x in d:
                if len(d[x]) == 1:
                    leaves.append(x)

            for leaf in leaves:
                neighbor = d[leaf][0]
                d[neighbor].remove(leaf)
                del d[leaf]

        return list(d.keys())
            
