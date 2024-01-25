class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        base = ""
        checker = ""
        if len(str1) >= len(str2):
            base = str2
            checker = str1
        else :
            base = str1
            checker = str2

        patten = ""
        i = 0
        subtochek = ""
        for c in base:
            patten += c
            i += 1
            subtochek = base[i:]
            if patten in subtochek and len(subtochek) % len(patten) == 0 :
                #print(patten)
                count = 0
                for j in range(0, len(subtochek), len(patten)) :
                    if patten != subtochek[j:j+len(patten)]:
                        break
                    else:
                        count = j+len(patten)
                if (count == len(subtochek)):
                    break
        print ("1 "+patten)
        if patten in checker and len(checker) % len(patten) == 0 :
            for j in range(0, len(checker), len(patten)) :
                if patten != checker[j:j+len(patten)]:
                    patten = ""
                    break
        else:
            patten = ""
        print ("2 "+patten)

        # find the greatest repeat of patten
        gcd = ""
        if patten != "" :
            try_count = len(base) // len(patten)
            print("3 "+str(try_count))
            last_good = ""
            for i in range(try_count, 0, -1):
                gcd = patten * i
                print("4 "+gcd)
                if len(base) % len(gcd) != 0 or len(checker) % len(gcd) != 0 :
                    continue
                for j in range(0, len(base), len(gcd)) :
                    if gcd != checker[j:j+len(gcd)]:
                        continue
                for j in range(0, len(checker), len(gcd)) :
                    if gcd != checker[j:j+len(gcd)]:
                        continue
                last_good = gcd
                break
            gcd = last_good

        print(gcd)
        return gcd

str1 = "ABABABAB"
str2 = "ABAB"

a = Solution()
r = a.gcdOfStrings(str1, str2)
