class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if n == 0:
            return True
        for i in range(length):
            is_current_empty = (flowerbed[i] == 0)
            is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            is_right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if is_current_empty and is_left_empty and is_right_empty:
                flowerbed[i] = 1

                n -= 1
                if n <= 0:
                    return True
        return False