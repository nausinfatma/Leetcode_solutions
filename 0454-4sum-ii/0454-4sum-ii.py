class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = {}

        for i in nums1:
            for j in nums2:
                s = i + j
                count[s] = count.get(s, 0) + 1

        cnt = 0

        for k in nums3:
            for l in nums4:
                target = -(k + l)
                cnt += count.get(target, 0)

        return cnt