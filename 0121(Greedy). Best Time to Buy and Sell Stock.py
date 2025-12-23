# Leetcode, Ligmaball
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 到目前為止的最低買價
        res = 0                   # 最大利潤

        for price in prices:
            # 如果今天更便宜，更新「買點」
            if price < min_price:
                min_price = price
            else:
                # 嘗試今天賣出
                res = max(res, price - min_price)

        return res
