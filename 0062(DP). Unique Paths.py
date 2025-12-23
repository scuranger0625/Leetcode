# Leetcode, Ligmaball
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 定義 # 2. 轉移
        dp= [[0]*(n) for _ in range(m)]

        # 3. 初始化
        for i in range(m):
            dp[i][n-1]=1
    
        for j in range(n):
            dp[m-1][j]=1

        # 4. 計算順序
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        # 5. 回答
        return dp[0][0]
