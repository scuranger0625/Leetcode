#include <bits/stdc++.h>
using namespace std;

// Leetcode, Ligmaball
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // graph[u] = {v, w}
        vector<vector<pair<int, int>>> graph(n + 1);

        for (auto& edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            graph[u].push_back({v, w});
        }

        // dist[i] 表示從 k 到 i 的最短距離
        vector<int> dist(n + 1, INT_MAX);
        dist[k] = 0;

        // priority_queue 預設是 max heap
        // 所以用 greater 變成 min heap
        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > pq;

        // {目前距離, 節點}
        pq.push({0, k});

        while (!pq.empty()) {
            auto [currentDist, node] = pq.top();
            pq.pop();

            // 如果這個距離已經不是最新最短距離，就跳過
            if (currentDist > dist[node]) continue;

            for (auto& [nextNode, weight] : graph[node]) {
                int newDist = currentDist + weight;

                if (newDist < dist[nextNode]) {
                    dist[nextNode] = newDist;
                    pq.push({newDist, nextNode});
                }
            }
        }

        int answer = 0;

        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) {
                return -1;
            }
            answer = max(answer, dist[i]);
        }

        return answer;
    }
};
