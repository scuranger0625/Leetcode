# 這個問題的前提是 : 我知道它裡面一定有鏡像存在。 
# 左邊開始撞到不對稱時 右邊的邊際就會相等的縮短至相同長度 目前最長的字串 
# 當最後撞到最終右邊縮短的邊際時 那答案就出來了
# 馬拉車演算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Step 1: 離散化（增強字串）
        # 思路：將原本的字串，每個字元之間插入'#'，讓奇偶長度的回文都可以統一處理
        # 例："aba" -> "#a#b#a#"
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        
        # Step 2: 初始化回文半徑列表
        # p[i] 表示以 t[i] 為中心，向左右最遠可以擴展多少格
        p = [0] * n
        
        # Step 3: 初始化中心 center 和最右邊界 right
        center = 0  # 當前回文的中心
        right = 0   # 當前回文的最右端（可達到的最大 i）
        
        # 同時記錄目前找到的最長回文的長度和中心位置
        max_len = 0
        max_center = 0
        
        # Step 4: 從第0項開始掃描
        for i in range(n):
            # (1) 計算鏡像位置 mirror
            # 思路：mirror = 2*center - i，這是基於對稱性
            mirror = 2 * center - i
            
            # (2) 如果 i 在目前最右邊界 right 之內，可以先初步設定 p[i]
            if i < right:
                # 可以利用 mirror 位置的回文長度來推估 p[i]
                # 但不能超過 right-i 的距離
                p[i] = min(right - i, p[mirror])
            
            # (3) 嘗試從 i 開始，向左右兩邊擴展
            # 思路：只要左右字符相同，就可以繼續擴展
            while (i + p[i] + 1 < n) and (i - p[i] - 1 >= 0) and (t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            
            # (4) 如果以 i 為中心的回文超出了目前 right
            # 思路：更新 center 和 right，因為新的回文更遠了
            if i + p[i] > right:
                center = i
                right = i + p[i]
            
            # (5) 同時記錄目前最長回文
            if p[i] > max_len:
                max_len = p[i]
                max_center = i
        
        # Step 5: 根據最長回文中心和半徑，還原出原始字串的子字串
        # 思路：
        # max_center 是增強字串中的中心點
        # max_len 是以 max_center 為中心，左右擴展的格數（不含 center）
        # 因為加了很多 '#'，所以要去掉
        start = (max_center - max_len) // 2  # 轉換回原始字串的起始位置
        
        return s[start:start + max_len]
