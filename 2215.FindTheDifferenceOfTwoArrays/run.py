class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        r1 = list(set(nums1))
        r2 = list(set(nums2))
        r = []
        for a in r1:
            if a in r2:
                r2.remove(a)
            else:
                r.append(a)

        return [r, r2]

