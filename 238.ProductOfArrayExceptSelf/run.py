class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        maxVal = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else :
                maxVal *= nums[i]
        result = []
        if zeroCount > 1:
            result = [ 0 for x in nums ]
        elif zeroCount == 1:
            result = [ 0 if x!=0 else maxVal for x in nums]
        else :
            result = [ maxVal // x for x in nums]
        return result
