# Leetcode, Ligmaball
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m：列數（有幾排）。grid 是「外層 list」，len(grid) 就是有幾列
        m =len(grid)    
        
        # n：行數（每排有幾格）。grid[0] 是第一列（第一排的那個 list），len(grid[0]) 就是欄數 
        # 題目保證是 m x n 矩陣，所以每一列長度都相同，用第一列即可代表 n
        n =len(grid[0])

        # dp[i][j]：從 (0,0) 走到 (i,j) 的最小路徑總和
        # 建立一個 m x n 的 DP 表，初始值先填 0，之後再逐格更新
        # for _ in range(m) 是在保證：每一列都是「新的獨立 list」。
        dp = [[0] * n for _ in range(m)]

        # 初始化
        dp[0][0] = grid[0][0]

        # 處理第一列（i = 0）在第一列中，只能從左邊 (0, j-1) 走到 (0, j)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        # 處理第一行（j = 0）在第一行中，只能從上面 (i-1, 0) 走到 (i, 0)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # 處理其餘格子（不是第一列、也不是第一行）
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+ grid[i][j] # 只能從上面或左邊來，取比較小的路徑再加上當前格子的值
        # 右下角就是從起點走到終點的最小路徑總和
        return dp[m-1][n-1]
