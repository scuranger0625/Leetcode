from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        parent = {}  # Union-Find 的父節點映射：parent[x] = y 代表 y 是 x 的父節點，根節點指向自己
        weight = {}  # weight[x] = x / parent[x] 的值（浮點數比例）
        
        def find(x: str) -> str:
            # 1. 如果 x 不在 parent，初始化
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
                return x
            
            # 路徑壓縮：如果父節點不是自己，就遞迴找 root
            if parent[x] != x:
                origin_parent = parent[x]
                root = find(origin_parent) # 遞迴find實現路徑壓縮
                
                # 更新權重
                weight[x] *= weight[origin_parent]
                # 更新父節點為 root（路徑壓縮）
                parent[x] = root
            
            return parent[x]
        
        def union(x: str, y: str, value: float):
            """            
            1. 初始化 x, y
            2. 找 rootX, rootY
            3. 若 root 不同，連接並計算權重
            """
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
            
            if y not in parent:
                parent[y] = y
                weight[y] = 1.0
            
            rootX = find(x)  # 找出 x 所屬集合的根節點，並在過程中做路徑壓縮與權重更新
            rootY = find(y)  # 找出 y 所屬集合的根節點，並在過程中做路徑壓縮與權重更新

            if rootX != rootY:
                parent[rootX] = rootY # 將rootx 指向 rooty
                weight[rootX] = weight[y] * value / weight[x] # 計算 rootX / rootY 的比例


        def isConnected(x: str, y: str) -> float:
            # 1. 若 x 或 y 不存在 → return -1.0
            if x not in parent or y not in parent:
                return -1.0
            rootX = find(x)  
            rootY = find(y)  
            # 2. 若 root 不同 → return -1.0
            if rootX != rootY:
                return -1.0
            # 3. 回傳 weight[x] / weight[y]
            return weight[x] / weight[y]
        
        # === 1. 建立 Union-Find 關係 ===
        for (a, b), val in zip(equations, values):
            union(a, b, val)
        
        # === 2. 回答查詢 ===
        result = []
        for c, d in queries:
            result.append(isConnected(c, d))
        
        return result
