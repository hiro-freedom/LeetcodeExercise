class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastIdx = len(nums)-1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] != 0:
                lastIdx = i
                break

        index = 0
        while index < lastIdx:
            if nums[index] == 0:
                nums.insert(lastIdx+1, 0)
                del nums[index : index+1]
                lastIdx -= 1
                #print(index)
                #print (lastIdx)
                #print(nums)
            else:
                index += 1

nums = [0,1,0,3,12]
a = Solution()
a.moveZeroes(nums)


