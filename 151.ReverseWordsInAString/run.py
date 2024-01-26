class Solution:
    def reverseWords(self, s: str) -> str:
        sTmp = s.strip(" ")
        sl = sTmp.split(" ")
        sll = [ x for x in sl if x!=""]
        sll.reverse()
        result = " ".join(sll)
        return result
