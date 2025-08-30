from typing import List, Optional
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 取得棋盤大小 row(m) column(n)
        m, n = len(board), len(board[0])
        # 特例: 搜尋剪枝 檢查字母數量是否有足夠格子來放
        word_count = Counter(word)  

        all_chars = [] # 用來存棋盤上的所有字母

        for row in board:
            for ch in row:
                all_chars.append(ch)
        
        board_count = Counter(all_chars)  # 統計棋盤字母次數

        # 如果棋盤上某個字母的數量不足以拼出 word，直接返回 False
        for ch, cnt in word_count.items(): # .items() 是字典（dict）的方法 它會一次取出鍵（key）和值（value）的成對資料。
            if board_count[ch] < cnt:
                return False
        
        def dfs(x, y, idx): # x, y：目前在棋盤的位置 idx：目前匹配到 word 的第幾個字母
            if idx == len(word):
                return True
            
            # 判斷x y是否超出範圍 以及棋盤的字母是否等於word的index
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx]:
                return False
            
            # 標記當前格子已訪問（避免走回頭路）
            tmp, board[x][y] = board[x][y], '#' # '#' 特殊字元 代表「這格暫時不可用」

            found = (dfs(x+1, y, idx+1) or # 下
                     dfs(x-1, y, idx+1) or # 上
                     dfs(x, y+1, idx+1) or # 右
                     dfs(x, y-1, idx+1))   # 左
            
            # 回溯：恢復原本的字母
            board[x][y] = tmp
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):  # idx=0 表示從 word 的第一個字母開始匹配
                    return True
        
        return False
        
