from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 定義dp 將dp[0]變成空字串
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        # k = 所有合法字串的集合
        for k in range(1, n+1):
            for i in range(k):
                # 對於任何一個合法解 都可以拆成多項式 Catalan（卡特蘭） 結構的典型分解
                for A in dp[i]:
                    for B in dp[k-1-i]:
                        dp[k].append("(" + A + ")" + B)
        
        return dp[n]
        
        


        
