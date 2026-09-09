class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        nums.sort()
        small = nums[:(n + 1) // 2][::-1]
        big = nums[(n + 1) // 2:][::-1]
        new = []

        for i in range((n+1)//2):
            new.append(small[i])

            if i < len(big):
                new.append(big[i])


        nums[:] = new