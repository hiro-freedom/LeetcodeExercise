#class Solution:
#    def maxArea(self, height: List[int]) -> int:
#        if len(height) < 2:
#            return 0
#        max1 = 0
#        idx1 = 0
#        max2 = 0
#        idx2 = 0
#        #if height[0] > height[1]:
#        #    max1 = height[0]
#        #    idx1 = 0
#        #    max2 = height[1]
#        #    idx2 = 1
#        #else:
#        #    max2 = height[0]
#        #    idx2 = 0
#        #    max1 = height[1]
#        #    idx1 = 1
#        for i in range(len(height)):
#            if max1 < height[i]:
#                max1 = height[i]
#                idx1 = i
#            elif max2 < height[i] and height[i] <= max1:
#                max2 = height[i]
#                idx2 = i
#        print (max1, max2)
#        print (idx1, idx2)
#
#        sqBase = max2 * abs(idx1 - idx2)
#        sq = 0
#        print(sqBase)
#        for i in range(len(height)-1):
#            if height[i] == 0:
#                continue
#            if (sqBase // height[i]) > (len(height) - i - 1) :
#                continue
#
#            for j in range(i, len(height)):
#                if height[j] == 0:
#                    continue
#                sq = min(height[i], height[j]) * (j-i)
#                if sq > sqBase:
#                    sqBase = sq
#                    print(sqBase)
#        return sqBase


# directly calc
#class Solution:
#    def maxArea(self, height: List[int]) -> int:
#        if len(height) < 2:
#            return 0
#
#        sq = 0
#        out = 0
#        for i in range(len(height)-1):
#            if height[i] == 0:
#                continue
#            for j in range(i, len(height)):
#                sq = min(height[i], height[j]) * (j-i)
#                if sq > out:
#                    out = sq
#        return out



class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        sq = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(height)):
            if height[i] == 0:
                continue
            for j in range(len(height)-1, i, -1):
                if height[j] >= height[i]:
                    sq1 = height[i] * (j-i)
                    break
            for j in range(i):
                if height[j] >= height[i]:
                    sq2 = height[i] * (i-j)
                    break
            if sq < max(sq1, sq2) :
                sq = max(sq1, sq2)

        return sq

