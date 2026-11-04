class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        
        heaters.sort()
        ans = 0

        for house in houses:
            left = 0
            right = len(heaters)

            
            while left < right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid

            
            dist_left = float('inf')
            dist_right = float('inf')

            if left > 0:
                dist_left = house - heaters[left - 1]

            if left < len(heaters):
                dist_right = heaters[left] - house

            closest = min(dist_left, dist_right)
            ans = max(ans, closest)

        return ans