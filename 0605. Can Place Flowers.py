#花圃不可以在鄰近的花盆連續種植 也就是說若是連續兩個數值為1 則為False

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 遍歷花圃列表，檢查是否可以種下 n 朵花
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0:
                # 檢查左邊和右邊地塊（如果存在）是否也是空的
                left_empty = (i == 0 or flowerbed[i-1] == 0)
                # i是否是最左邊的或i+1是否有種植花朵
                right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1  # 在當前地塊種花
                    n -= 1  # 減少需要種的花的數量
                    # 跳過下一個地塊，因為不能在相鄰地塊種花
                    i += 1
            # 遍歷下一個地塊
            i += 1
        
        # 如果遍歷結束後仍有花沒有種下，返回 False，否則返回 True
        return n <= 0
            
        
