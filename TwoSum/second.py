# the fastest way I found.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i in range(len(nums)):
            mymap[nums[i]] = i

        for i in range(len(nums)):
            toCheck = target - nums[i]
            if (toCheck in mymap) and (mymap[toCheck] != i):
                 return [i, mymap[toCheck]]

