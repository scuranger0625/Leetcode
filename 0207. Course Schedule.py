from collections import deque, defaultdict
from typing import List

class Solution:
    # Kahn Algorithm
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: 建立鄰接表（graph）與入度表（indeg）
        graph = defaultdict(list)    # graph[b] 存放「修 b 之後可以修的課」
        indeg = [0] * numCourses     # indeg[i] 記錄課 i 的入度
        
        # 迭代 prerequisites，填充 graph 和 indeg
        for a, b in prerequisites:
            # 將 b 加入 a 之後 (先修b 才能修a)
            graph[b].append(a)
            # 記錄課程 a 還有多少前置課沒修
            indeg[a] += 1
        
        # Step 2: 找出入度為 0 的課放入佇列
        queue = deque()

        for i in range(numCourses): # 初始化 queue，把所有 indeg[i] == 0 的 i 放進 deque
            if indeg[i] == 0:
                queue.append(i)


        # Step 3: BFS 消入度
        taken = 0  # 已經修過的課數

        # 當 queue 不為空時，反覆取出課程 cur
        while len(queue) != 0:  
            cur = queue.popleft()  # 從佇列取出當前可修的課程（入度為 0），準備處理它解鎖的後續課 (重要)
            # 修掉一門課，計數 +1
            taken += 1
            # 遍歷 graph[cur] 的所有後續課程 nxt
            for nxt in graph[cur]:
                indeg[nxt] -= 1 # 這堂課的入度 -1
                
                # 如果入度變成 0，加入 queue (已經可選修)
                if indeg[nxt] ==0:
                    queue.append(nxt)
        # Step 4: 檢查是否修完全部課
        return taken == numCourses
