from typing import List

"""
策略步驟（分桶 + 貪婪）
1.從第一天開始掃，找到第一個低點（買入點）
2.往後走，直到遇到第一個下跌日，把前一天當成最高點（賣出點）
3.記錄這一桶的利潤 = 賣價 - 買價
4.從這個賣出日之後繼續找下一桶
5.重複直到結束
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        i = 0 # 從第一天開始

        # 只要還沒到最後一天就繼續找買賣機會
        while i < n-1:
            # Step 1: 找谷底（買點）
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            buy = prices[i] # 記錄購買價格

            # Step 2: 找峰頂（賣點）
            while i < n-1 and prices[i] < prices[i+1]:
                i += 1
            sell = prices[i] # 紀錄售出價格

            # Step 3: 累加這一桶的利潤
            profit += sell - buy
        
        return profit


        
