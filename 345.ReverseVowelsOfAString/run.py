class Solution:
    def reverseVowels(self, s: str) -> str:
        vList = []
        sl = list(s)
        for i in range(len(sl)) :
            if sl[i] in 'aeiouAEIOU':
                vList.append(sl[i])
                sl[i] = 'a'
        vList.reverse()
        j = 0
        for i in range(len(sl)) :
            if sl[i] == 'a':
                sl[i] = vList[j]
                j += 1
        result = "".join(sl)
        return result
