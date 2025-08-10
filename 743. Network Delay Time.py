import heapq  # 最小堆（優先佇列），用於取出當前距離最小的節點
from collections import defaultdict  
from typing import List           

class Solution:
    # Dijkstra Algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 建立鄰接表
        graph = defaultdict(list)
        # u: 起點 v: 終點 w: wi 是訊號從 ui 傳送到 vi 所需的時間（單位為正整數）
        for u, v, w in times:
            graph[u].append((v, w))  # 從 u 到 v 的邊，權重 w
        
        
        distance = {i: float('inf') for i in range(1, n + 1)}  # 設置距離為無限大
        distance[k] = 0 # 設置起點 k = 0
        heap = [(0, k)] # (距離, 節點)

        # Dijkstra 主迴圈
        while heap:
            # d :當前所有待處理節點中最小的
            d, node = heapq.heappop(heap) # heapq.heappop 會把 距離最小 的元素從堆中取出，並回傳它。
            # 若當前d距離 > 當前節點 無視他
            if d > distance[node]:
                continue
            
            # nei : neighbor（鄰居節點）
            for nei, w in graph[node]:
                # 如果從 node 經過這條邊到 nei 的距離更短，就更新
                if d + w < distance[nei]:
                    distance[nei] = d + w # 更新最短路徑
                    heapq.heappush(heap, (d + w, nei)) # 首次從堆積pop彈出時 確認最短路徑
           
        # 所有節點的最短距離中取最大值（因為訊號必須到達最慢的那個節點才算全部收到）
        max_dist = max(distance.values())
        # 如果還有節點距離是無限大，代表它沒收到訊號 → 回傳 -1
        return max_dist if max_dist < float('inf') else -1





        
