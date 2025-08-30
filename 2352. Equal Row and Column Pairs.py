class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # 將矩陣轉置
        n = len(grid)
        transpose = [[grid[j][i] for j in range(n)] for i in range(n)]

        # 計算行和列相同的對數
        count = 0
        for row in grid:
            for col in transpose:
                if row == col:
                    count += 1

        return count
        
