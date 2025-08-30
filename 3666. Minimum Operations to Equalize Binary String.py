from collections import deque  # BFS 佇列

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        """
        - 只看狀態 Z = 目前字串中 '0' 的個數（0..n）。
        - 一次操作選 t 個 0、(k - t) 個 1 翻轉，Z 會變成 Z' = Z + k - 2t。
        - 可達的 Z' 在某一段 [L, R] 之內，且與 (Z + k) 同奇偶，步長為 2。
        - 在 Z 的狀態圖上用 BFS 尋找從 Z0 到 0 的最短步數。
        - 為了避免逐一掃整段 [L, R]，用「同奇偶跳表」（find-next + 路徑壓縮）一次拔除
          尚未拜訪的 Z'，總複雜度 ~ O(n α(n))。
        """

        # 題目要求：中途存輸入（不一定要用它來計算）
        drunepalix = s

        n = len(s)
        Z0 = s.count('0')  # 初始 '0' 的數量
        if Z0 == 0:
            return 0  # 本來就全為 1

        # 特例：k == n -> 每次必翻整串，只會在 s 與 ~s 之間來回
        # 想成全 1 的唯一可能：原本就是全 1（上面已回 0），或原本全 0（翻一次）
        if k == n:
            return 1 if Z0 == n else -1

        # 不可能情況：k 偶數時，Z 的奇偶性永不改變；若起始 Z 為奇數，無法到 0（偶數）
        if (k & 1) == 0 and (Z0 & 1) == 1:
            return -1

        # dist[z] = 抵達「有 z 個 0」的最少步數；初始化為無限大
        INF = 10**18
        dist = [INF] * (n + 1)
        dist[Z0] = 0

        # === 同奇偶跳表（find-next 結構）===
        # 我們維護兩張「下一個尚未拜訪的 index」表：
        #   next_even: 只關注偶數 z；next_odd: 只關注奇數 z
        # 其他奇偶的 index 先指到下一個位置，達到「跨奇偶預先跳過」的效果。
        def build_next(parity: int):
            # parity = 0（偶）或 1（奇）
            # 初始：nxt[i] = i，自迴圈；把不符 parity 的 i 直接指向 i+1。
            nxt = list(range(n + 3))
            for i in range(parity ^ 1, n + 1, 2):
                nxt[i] = i + 1  # 先跨過另一種奇偶
            # 邊界保護位
            nxt[n + 1] = n + 1
            nxt[n + 2] = n + 2
            return nxt

        next_even = build_next(0)
        next_odd  = build_next(1)

        # 迭代式 find（帶路徑壓縮）：回傳「>= x 的下一個尚未拜訪、且符合該跳表奇偶」的位置
        def find(nxt, x: int) -> int:
            while nxt[x] != x:
                nxt[x] = nxt[nxt[x]]  # 路徑壓縮
                x = nxt[x]
            return x

        # 將 x 標記為「已拜訪」：把它連到同奇偶的下一個（+2）
        def erase(nxt, x: int):
            nxt[x] = find(nxt, x + 2)

        # 起點 Z0 從對應奇偶的跳表移除，避免之後再被拜訪
        if (Z0 & 1) == 0:
            erase(next_even, Z0)
        else:
            erase(next_odd, Z0)

        # BFS 佇列（只在 Z 的空間 0..n 上移動）
        q = deque([Z0])
        append = q.append
        popleft = q.popleft
        dist_arr = dist  # 綁成區域變數，微幅加速

        while q:
            Z = popleft()
            d = dist_arr[Z]
            O = n - Z  # 目前 '1' 的數量

            # t 的可選範圍：必須同時滿足 t ≤ Z（可翻的 0 夠）、k - t ≤ O（可翻的 1 夠）
            #   -> t ≥ k - O，t ≥ 0，t ≤ Z，t ≤ k
            tl = 0 if k <= O else k - O
            tr = k if k <= Z else Z
            if tl > tr:
                continue  # 無法進行任何合法翻轉

            # 可達 Z' = Z + k - 2t
            # 當 t 從 tr 降到 tl，Z' 從最小 L 遞增到最大 R（等差，步長 2）
            L = Z + k - (tr << 1)  # tr*2 用位移
            R = Z + k - (tl << 1)
            if L < 0: L = 0
            if R > n: R = n

            # 這一段 Z' 的奇偶固定為 (Z + k) % 2（因為 -2t 只改變偶數）
            parity = (Z + k) & 1
            nxt = next_even if parity == 0 else next_odd

            # 從 L 對齊到該奇偶的第一個點，然後用 find-next「拉掉」整段未訪問節點
            i = L if (L & 1) == parity else L + 1
            i = find(nxt, i)
            while i <= R:
                if dist_arr[i] == INF:
                    dist_arr[i] = d + 1   # 第一次抵達 i（Z=i）的最短步數
                    append(i)             # 入佇列做後續擴展
                erase(nxt, i)             # 標記 i 已訪問（跳到 i+2）
                i = find(nxt, i)          # 找下一個尚未訪問且同奇偶的節點

        # 若 0（全為 1 的狀態）仍為 INF，代表不可達；否則回最短步數
        return -1 if dist_arr[0] == INF else dist_arr[0]
