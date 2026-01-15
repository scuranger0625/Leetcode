# Leetcode, Ligmaball
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 因為是無向圖，Bellman-Ford 要把每條邊拆成雙向
        bf_edges = []
        for u, v, w in edges:
            bf_edges.append((u, v, w))
            bf_edges.append((v, u, w))

        # Bellman-Ford：從 src 出發，回傳「門檻內可達城市數」
        def bellman_ford_count(src: int) -> int:
            INF = 10**18
            dist = [INF] * n
            dist[src] = 0

            # 最多跑 n-1 輪鬆弛
            for _ in range(n - 1):
                updated = False

                for u, v, w in bf_edges:
                    # 若 u 還不可達，跳過
                    if dist[u] == INF:
                        continue

                    nd = dist[u] + w

                    # 剪枝：我們只在乎 ≤ threshold
                    if nd > distanceThreshold:
                        continue

                    if nd < dist[v]:
                        dist[v] = nd
                        updated = True

                # 若這一輪完全沒更新，可以提前結束
                if not updated:
                    break

            # 計算可達城市數（不含自己）
            count = 0
            for i in range(n):
                if i != src and dist[i] <= distanceThreshold:
                    count += 1

            return count

        # 找「可達城市數最少」的城市，平手選編號最大的
        best_count = 10**18
        best_city = -1

        for city in range(n):
            cnt = bellman_ford_count(city)
            if cnt < best_count or (cnt == best_count and city > best_city):
                best_count = cnt
                best_city = city

        return best_city
