class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        buf1 = []
        buf2 = []
        buf = [buf1, buf2]
        idx = -1
        c = 0
        only1 = True

        for i in range(len(nums)):
            if nums[i] == 1:
                if idx < 0 :
                    idx = 0
                buf[idx].append(1)
            else :
                only1 = False
                if len(buf[0]) + len(buf[1]) > 0:
                    # switch buffer
                    c = max(c, len(buf[0]+buf[1]))
                    idx = (idx + 1) % 2
                    buf[idx].clear()
                else :
                    idx = -1

        c = max(c, len(buf[0]+buf[1]))
        if only1 : 
            c = c - 1

        return c

