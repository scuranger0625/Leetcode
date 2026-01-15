class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0 # 初始化利潤 
        hold  = -prices[0] # 如果你在第 0 天買入，利潤會變成 0 - prices[0] 所以是負的

        for price in prices[1:]:
            # 先準備一個暫存 因為等一下更新 hold 會用到「舊的 cash」
            prev_cash = cash
            # 現在更新 cash：
            cash = max(cash, hold+price - fee)
            # 更新 hold (今天要不要買?)
            hold = max(hold, prev_cash - price)

        return cash
