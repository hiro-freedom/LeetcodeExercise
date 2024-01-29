import sys

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        left = sys.maxsize
        mid = sys.maxsize
        for i in range(0, len(nums)):
            if left > nums[i]:
                left = nums[i]
            elif nums[i] > left and nums[i] < mid:
                mid = nums[i]
            elif nums[i] > mid:
                return True
        return False

nums = [1,5,0,4,1,3]
#[0,4,2,1,0,-1,-3]
a = Solution()
r = a.increasingTriplet(nums)
print(r)
