# Leetcode, Ligmaball
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 定義 轉移 初始化 計算 回答
        ans= [0]*(n+1)

        for i in range(1,n+1):
            ans[i] = ans[i//2]+(i%2)

        return ans
        


