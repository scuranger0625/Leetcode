# Leetcode, Ligmaball
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # 1.定義 2.轉移
        a = cost[0]
        b = cost[1]
        # 3.初始化
        for i in range(2,n):
            # 4.計算順序
            c = min(a,b)+cost[i]
            a=b
            b=c
        # 5.回答
        return min(a,b)
