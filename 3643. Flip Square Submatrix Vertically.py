class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # 垂直翻轉 (vertical flip)：交換子矩陣上、下兩列
        # 子矩陣左上角在 (x, y)，邊長為 k
        for i in range(k // 2):                 # 只需要交換一半的行數
            top = x + i
            bottom = x + k - 1 - i
            for j in range(k):                  # 對每一欄做交換
                c = y + j
                grid[top][c], grid[bottom][c] = grid[bottom][c], grid[top][c]
        return grid
