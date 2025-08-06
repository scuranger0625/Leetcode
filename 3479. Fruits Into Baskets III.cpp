#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

// Fenwick 樹 (Binary Indexed Tree) 類別
// 用於在一維範圍內快速做 "加值" 與 "區間和" 查詢
class Fenwick {
public:
    int n;                // Fenwick 樹大小
    vector<int> bit;      // 存儲樹狀陣列（1-indexed）

    Fenwick() {}
    Fenwick(int _n): n(_n), bit(_n + 1, 0) {}

    // 在位置 i (0-indexed) 加上 v
    void update(int i, int v) {
        // 內部用 1-indexed 遍歷
        for (++i; i <= n; i += i & -i)
            bit[i] += v;
    }

    // 查詢區間 [0..i] 的前綴和
    int query(int i) const {
        int s = 0;
        for (++i; i > 0; i -= i & -i)
            s += bit[i];
        return s;
    }

    // 查詢區間 [l..r] 的和
    int range_query(int l, int r) const {
        if (l > r) return 0;
        return query(r) - (l > 0 ? query(l - 1) : 0);
    }
};

// Solution 類別實作「樹中有樹」結構：
// 外層線段樹 + 內層 Fenwick 樹
class Solution {
public:
    int n;                             // 原始 baskets 大小
    int size;                          // 線段樹底層節點數（最小 2^k >= n）
    vector<vector<int>> coords;        // 每個節點的 "值域壓縮" 列表：存該區間所有籃子容量
    vector<Fenwick> bits;              // 對應每個節點的 Fenwick 樹，管理 "該節點區間" 的可用數量
    vector<int> baskets;               // 原始籃子容量陣列

    // build(): 建立 2D 結構
    // 1) 外層：線段樹節點各自保有子區間的容量列表 coords[node]
    // 2) 內層：使用 Fenwick 管理每個容量出現的頻次 (1 = 可用, 0 = 已用)
    void build(const vector<int>& b) {
        baskets = b;
        n = b.size();
        // 計算線段樹底層節點數
        size = 1;
        while (size < n) size <<= 1;
        coords.assign(2 * size, {});
        bits.assign(2 * size, Fenwick());

        // 1) 葉節點：收集各自對應的位置的容量值
        for (int i = 0; i < n; ++i) {
            coords[size + i].push_back(baskets[i]);
        }
        // 2) 自底向上合併左右子區，並做去重、排序
        for (int node = size - 1; node > 0; --node) {
            auto &L = coords[node << 1];       // 左子區列表
            auto &R = coords[(node << 1) | 1]; // 右子區列表
            auto &C = coords[node];            // 當前節點列表
            C.reserve(L.size() + R.size());
            C.insert(C.end(), L.begin(), L.end());
            C.insert(C.end(), R.begin(), R.end());
            sort(C.begin(), C.end());
            C.erase(unique(C.begin(), C.end()), C.end());
        }
        // 3) 初始化每個節點的 Fenwick 樹，長度等於 coords[node].size()
        for (int node = 1; node < 2 * size; ++node) {
            bits[node] = Fenwick(coords[node].size());
        }
        // 4) 將所有籃子 "加入" 相應節點的 Fenwick（頻次 +1）
        //    葉 -> 根 路徑上更新，以便節點內都能查到
        for (int i = 0; i < n; ++i) {
            int val = baskets[i];
            int node = size + i;
            while (node > 0) {
                // 找到 val 在 coords[node] 中的下標
                int pos = lower_bound(coords[node].begin(), coords[node].end(), val)
                          - coords[node].begin();
                bits[node].update(pos, 1);
                node >>= 1;
            }
        }
    }

    // query(fruit): 在 "樹中有樹" 上尋找最左側能放下 fruit 的籃子 index
    // 返回 0..n-1 或 -1
    int query(int fruit) {
        // 根節點先檢查：若根區間內沒有 >= fruit 的值，直接 -1
        auto &root = coords[1];
        int p0 = lower_bound(root.begin(), root.end(), fruit) - root.begin();
        if (p0 == (int)root.size() || bits[1].range_query(p0, root.size() - 1) == 0)
            return -1;

        int node = 1, l = 0, r = size;
        // 從根往下二分決定走左走右
        while (node < size) {
            int mid = (l + r) >> 1;
            int left = node << 1, right = left | 1;
            // 在左子區的 coords[left] 找 >= fruit 的下標 posL
            auto &CL = coords[left];
            int posL = lower_bound(CL.begin(), CL.end(), fruit) - CL.begin();
            // 如果左子區 posL..end 有可用頻次 >0，就往左；否則往右
            if (posL < (int)CL.size() && bits[left].range_query(posL, CL.size()-1) > 0) {
                node = left;
                r = mid;
            } else {
                node = right;
                l = mid;
            }
        }
        // 到葉節點：即該葉子對應的籃子位置
        return node - size;
    }

    // update(idx): "移除" idx 號籃子
    // 透過從葉 -> 根路徑上將原先 update(+1) 的位置 update(-1)
    void update(int idxBasket) {
        int node = size + idxBasket;
        int val = baskets[idxBasket];
        while (node > 0) {
            auto &C = coords[node];
            int pos = lower_bound(C.begin(), C.end(), val) - C.begin();
            bits[node].update(pos, -1);
            node >>= 1;
        }
    }

    // 主函式：依序對 fruits 進行配對，統計無法配對數量
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        build(baskets);
        int unplaced = 0;
        for (int fruit : fruits) {
            int idx = query(fruit);
            if (idx == -1) {
                ++unplaced;
            } else {
                update(idx);
            }
        }
        return unplaced;
    }
};
