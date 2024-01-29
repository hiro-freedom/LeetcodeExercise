class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        base = 0
        count = 0
        for i in range(0, len(nums) - 1):
            base = nums[i]
            count = 0
            for j in range(i+1, len(nums)):
                if base < nums[j]:
                    if count == 0:
                        base = nums[j]
                        count += 1
                    else :
                        return True
                else:
                    if count > 0 and base > nums[j] and nums[j] > nums[i]:
                        base = nums[j]
        return False

nums = [1,5,0,4,1,3]
#[0,4,2,1,0,-1,-3]
a = Solution()
r = a.increasingTriplet(nums)
print(r)
