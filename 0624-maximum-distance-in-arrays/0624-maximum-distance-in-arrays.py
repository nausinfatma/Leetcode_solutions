class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        
        glo_min = arrays[0][0]
        glo_max = arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):

            max_dist = max(
                max_dist,
                arrays[i][-1] - glo_min,
                glo_max - arrays[i][0]
            )

            glo_min = min(glo_min, arrays[i][0])
            glo_max = max(glo_max, arrays[i][-1])

        return max_dist