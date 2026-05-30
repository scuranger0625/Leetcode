# Leetcode, Ligmaball
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        # adjacency list
        for u, v, w in flights:
            graph[u].append((v, w))

        # dist[node][edges_used]
        dist = [
            [float('inf')] * (k + 2)
            for _ in range(n)
        ]

        dist[src][0] = 0

        # (cost, node, edges_used)
        heap = [(0, src, 0)]

        while heap:

            cost, node, edges_used = heapq.heappop(heap)

            # edge 超標
            if edges_used > k + 1:
                continue

            # 抵達終點
            if node == dst:
                return cost

            # 擴展鄰居
            for nei, price in graph[node]:

                new_cost = cost + price
                new_edges = edges_used + 1

                # 合法且更優
                if (
                    new_edges <= k + 1
                    and
                    new_cost < dist[nei][new_edges]
                ):

                    dist[nei][new_edges] = new_cost

                    heapq.heappush(
                        heap,
                        (
                            new_cost,
                            nei,
                            new_edges
                        )
                    )

        return -1
