# Leetcode, Ligmaball
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # dp 會存整個 Pascal 三角形
        dp =[]

        for i in range(numRows):
            row = [0]*(i+1)
            # 每一列的第一個與最後一個一定是 1 (Pascal 三角形特性)
            row[0]=1
            row[-1]=1

            for j in range(1,i):
                # 上一列的左上 + 右上
                row[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(row)

        return dp
