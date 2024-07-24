#有 n 個小朋友，每個小朋友都有一些糖果。你有一個整數數組 candies，其中 candies[i] 表示第 i 個小朋友擁有的糖果數量，
#還有一個整數 extraCandies，表示你擁有的額外糖果數量。
#返回一個布林數組 result，其長度為 n，其中 result[i] 為 true 表示給第 i 個小朋友所有的額外糖果後，
#他們擁有的糖果數量將是所有小朋友中最多的，否則為 false。
#注意，可以有多個小朋友擁有最多的糖果數量。

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mylist = []
        # max函數計算資料裡面的最大值 
        maxnum = max(candies)
        for i in candies:
            # >=計算糖果數量+額外糖果是否大於等於最大值 若是則跑出True 反之則是False
            mylist.append(i + extraCandies >= maxnum)
        
        return mylist
