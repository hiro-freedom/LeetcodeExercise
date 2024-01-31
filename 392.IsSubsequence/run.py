class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        index = 0
        found = False
        for i in range(len(s)):
            found = False
            for j in range(index, len(t)):
                if t[j] == s[i]:
                    index = j+1
                    found = True
                    break
            if not found :
                return False

        return found

