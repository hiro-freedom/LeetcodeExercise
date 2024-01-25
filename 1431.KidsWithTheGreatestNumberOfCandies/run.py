class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        minVal = maxVal - extraCandies
        result = [ x >= minVal for x in candies]
        return result
