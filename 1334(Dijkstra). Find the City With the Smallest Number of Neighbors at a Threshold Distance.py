# Leetcode, Ligmaball
class Solution:
    # Dijkstra Algorithms
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 準備鄰接矩陣 (無向加權圖)
        graph = [[] for _ in range(n)]

        # 把edges放進去(雙向)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # 寫一個內部函式：從 src 跑 Dijkstra，回傳「門檻內可達城市數」
        def dijkstra_count(src: int) -> int:
            # 距離一開始都很大（無限大）起點到自己距離是 0
            # 1. 初始化距離陣列
            INF = 10**18
            dist = [INF] * n
            dist[src] = 0  # src = 起點

            # 2.建立 priority queue
            pq = [(0, src)]

            # 3.開始跑 while 迴圈
            while pq:
                d, u = heapq.heappop(pq)  # d : 從heap拿出來的候選距離 u : 節點

                # 4. 丟掉過期資料（關鍵）
                if d != dist[u]:
                    continue

                # 5. 小技巧：可提早停止（因為有 threshold）
                if d > distanceThreshold:
                    break

                # 6. 鬆弛操作鄰居
                for v, w in graph[u]:
                    # nd = 走到鄰居 v 的新距離
                    nd = d + w

                    # 因為我們只在乎 ≤ threshold，先剪枝：
                    if nd > distanceThreshold:
                        continue

                    # 如果更短，更新並丟回 heap：
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))

            # 7. 算可達數（不含自己）
            count = 0
            for i in range(n):
                if i != src and dist[i] <= distanceThreshold:
                    count += 1
            return count

        # 3) 對每個城市跑一次 Dijkstra，找「可達城市數最少」者；平手選編號最大
        # 先準備「目前最佳」：
        best_count = 10**18
        best_city = -1

        # 遍歷每個城市
        for city in range(n):
            cnt = dijkstra_count(city)

            # 更新規則是：先比 cnt：越小越好 平手選 編號更大（題目要求）
            if cnt < best_count or (cnt == best_count and city > best_city):
                best_count = cnt
                best_city = city

        return best_city
