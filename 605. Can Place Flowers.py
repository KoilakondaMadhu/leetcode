class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                emptyleftplot = (i == 0) or (flowerbed[i - 1] == 0)
                emptyrightlot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if emptyleftplot and emptyrightlot:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
             
