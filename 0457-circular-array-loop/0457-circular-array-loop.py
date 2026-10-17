class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            slow = fast = i
            direction = nums[i] > 0

            while nums[slow] * (1 if direction else -1) > 0 and \
                  nums[fast] * (1 if direction else -1) > 0:

                next_slow = next_index(slow)
                next_fast = next_index(fast)

                if nums[next_fast] * (1 if direction else -1) <= 0:
                    break

                next_fast = next_index(next_fast)

                if nums[next_fast] * (1 if direction else -1) <= 0:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow != next_index(slow):
                        return True
                    break

            
            slow = i
            while nums[slow] * (1 if direction else -1) > 0:
                nxt = next_index(slow)
                nums[slow] = 0
                slow = nxt

        return False
