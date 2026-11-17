class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        edges = {}

        for row in wall:
            curr = 0

            for brick in row[:-1]:
                curr += brick
                edges[curr] = edges.get(curr, 0) + 1

        return len(wall) - max(edges.values(), default=0)