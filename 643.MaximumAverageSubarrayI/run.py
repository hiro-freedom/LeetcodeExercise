class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k :
            return 0

        m = sum(nums[0: k])
        s = m
        for i in range(1, len(nums) - k + 1) :
            s = s - nums[i-1] + nums[i+k-1]
            m = max(m, s)
        return m/k

