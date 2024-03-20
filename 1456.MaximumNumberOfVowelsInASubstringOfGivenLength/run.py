class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k ==0 or len(s) == 0:
            return 0

        if len(s) < k :
            k = len(s)

        s.lower()
        v = "aeiou"
        c = 0
        for i in range(k) :
            if s[i] in v:
                c += 1
        m = c
        for i in range(1, len(s) - k+1) :
            if s[i+k-1] in v:
                c += 1
            if s[i-1] in v:
                c -= 1
            if c == k :
                return k
            m = max(m, c)
        return m

