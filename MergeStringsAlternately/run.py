
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        last = 0
        for i in range(min(len(word1), len(word2))) :
            result += word1[i] + word2[i]
            last = i
        last += 1
        print(last)
        result += word1[last:] if last < len(word1) else word2[last:]
        return result

w1 = "ab"
w2 = "pqrs"
a = Solution()
r = a.mergeAlternately(w1, w2)
print(r)

