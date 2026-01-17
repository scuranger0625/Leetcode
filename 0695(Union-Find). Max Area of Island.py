# Leetcode, Ligmaball
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m= len(grid) # 列狀態
        n= len(grid[0]) # 行狀態
        
        # 建立一個長度 m*n 的陣列，裡面放的是 0, 1, 2, 3, ..., m*n-1
        parent = [i for i in range(m*n)]
        size = [0]*(m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    # 每一個節點，都必須有唯一編號 
                    # i*n 先把「第幾列」拉開距離
                    # 每一列佔用一整段 [i*n, i*n + n-1]
                    # 不同列 永遠不可能重疊
                    size[i*n + j]=1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # 路徑壓縮
            return parent[x]

        def union(x,y):
            rx = find(x) # 找出 x 所屬島嶼的代表
            ry = find(y) # 找出 y 所屬島嶼的代表
            
            # 防止重複合併、也是正確性的保證
            if rx != ry:
                parent[ry]= rx # 讓 y 那座島，併到 x 那座島底下
                size[rx]+= size[ry] # 島的面積相加
        # 按秩合併
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    cur = i*n + j

                    # 檢查右邊
                    if j+1 < n and grid[i][j+1]==1:
                        union(cur, i*n + (j+1))

                    # 檢查下邊
                    if i+1 < m and grid[i+1][j]==1:
                        union(cur, (i+1)*n+j)
        ans=0
        for i in range(m*n):
            if parent[i] ==i:# 只看島的代表
                ans = max(ans, size[i])

        return ans

