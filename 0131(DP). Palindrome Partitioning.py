# Leetcode, Ligmaball
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 定義：isPal[i][j] 表示 s[i:j+1] 是否為回文 ,開一張 n x n 的表，準備記錄每個子字串 s[i:j+1] 是否為回文。
        isPal = [[False]* n for _ in range(n)]

        # 因為待會會用到 isPal[i+1][j-1]，也就是「右下角」的子問題；你必須先算好它，現在從右往左才保證用到的值已經存在。
        # 初始化 + 計算順序（區間 DP）
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                """
                s[i] == s[j] 回文兩端一定要相等。
                (j - i <= 1 or isPal[i+1][j-1])
                如果長度 ≤ 2（也就是 j-i 是 0 或 1），兩端相等就直接是回文："a"、"aa"
                否則就看中間那段 s[i+1 : j] 是否回文（由 isPal[i+1][j-1] 提供）
                """
                if s[i] == s[j] and (j - i <= 1 or isPal[i+1][j-1]):
                    isPal[i][j] = True

        # 定義：dp[i] = 從 i 開始的所有切割方式    
        dp =[[] for _ in range(n+1)]

        # 初始化（base case）
        dp[n] = [[]]

        # 計算順序（從後往前)
        for i in range(n - 1, -1, -1):
            for j in range(i,n):
                if isPal[i][j]:
                    for tail in dp[j+1]:
                        dp[i].append([s[i:j+1]]+tail)

        return dp[0]
        
