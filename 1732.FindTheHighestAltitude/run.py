class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        m = 0

        for i in range(len(gain)):
            h = h + gain[i]
            if gain[i] > 0 :
                m = max(h, m)

        return m

