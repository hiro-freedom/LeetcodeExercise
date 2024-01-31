class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            else:
                if nums[l] + nums[r] > k:
                    r -= 1
                else:
                    l += 1
        return count 

# directly way. work but exceed time limit
#class Solution:
#    def maxOperations(self, nums: List[int], k: int) -> int:
#        found = True
#        count = 0
#        left = 0
#        while found:
#            found = False
#            for i in range(len(nums)-1):
#                if nums[i] > k:
#                    continue
#                left = k - nums[i]
#                for j in range(i+1, len(nums)):
#                    if nums[j] == left:
#                        del nums[j]
#                        found = True
#                        break
#                if found :
#                    del nums[i]
#                    count += 1
#                    break
#
#        return count

n = [1,2,3,4]
k = 5
a = Solution()
r = a.maxOperations(n,k)
print(r)
