class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        a = len(nums) - 1
        idx = 0
        l = sum(nums[:idx])
        r = sum(nums[idx+1:])
        if l == r :
            return idx

        while idx < a:
            l = l + nums[idx]
            r = r - nums[idx+1]
            idx = idx + 1

            if l == r:
                return idx

        return -1

