# Leetcode, Ligmaball
class Solution:
    def numTrees(self, n: int) -> int:
        # 建立 dp 陣列，dp[i] = i 個節點的 BST 數量
        dp = [0] * (n + 1)
        # 初始化
        dp[0]=1
        dp[1]=1
        # 從 2 個節點開始算
        for nodes in range(2, n+1):
            for root in range(1, nodes+1):
                dp[nodes]+=dp[root-1]*dp[nodes-root] # DP狀態轉移 root決定剩下來的nodes的組合數乘積

        return dp[n]
