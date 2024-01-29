class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 0:
            return 0
        cur = chars[0]
        offset = 0
        size = 1
        #index = 1

        while (offset+size) < len(chars):
            print (offset, size)
            if chars[offset + size] == cur :
                size += 1
            else:
                if size == 1:
                    cur = chars[offset + size]
                    offset += 1
                else :
                    del chars[offset+1 : offset+size]
                    print(chars)
                    strSize = str(size)
                    for i in range(len(strSize)):
                        chars.insert(offset + 1 + i, strSize[i])
                    offset += len(strSize) + 1
                    if offset < len(chars) :
                        cur = chars[offset]
                        size = 1
                    else :
                        break
        if size > 1:
            del chars[offset+1 : offset+size]
            strSize = str(size)
            for i in range(len(strSize)):
                chars.insert(offset + 1 + i, strSize[i])


        return len(chars)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#chars = ["a","a","b","b","c","c","c"]
a = Solution()
r = a.compress(chars)
print(chars)
