class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        newbed = [0] + flowerbed + [0]
        count = 0
        canPlace = 0
        print(newbed)
        for i in range(0, len(newbed)):
            if newbed[i] == 0 :
                count += 1
            else:
                print(count)
                canPlace += (count+1) // 2 - 1
                count = 0
        if count != 0:
            print(count)
            canPlace += (count+1) // 2 - 1
            count = 0
        #count = 0
        #if len(flowerbed) > 2:
        #    # process the middle
        #    for i in range(1, len(flowerbed)-1):
        #        if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0 :
        #            count += 1
        #    # process the begin and end
        #    if flowerbed[0] + flowerbed[1] == 0:
        #        count += 1
        #    if flowerbed[-1] + flowerbed[-2] == 0:
        #        count += 1
        #elif len(flowerbed) <= 2:
        #    if sum(flowerbed) == 0:
        #        count = 1

        return n <= canPlace 


l = [1,0,0,0,1,0,0]
n = 2
a = Solution()
r = a.canPlaceFlowers(l, n)
print(r)

