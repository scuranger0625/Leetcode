# Leetcode, Ligmaball
class Solution:
    # List Scheduling Algorithm
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. 統計每個任務的次數
        freq = Counter(tasks)

        # 2. Max heap：(-count, task)
        heap = []
        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))

        # 3. 冷卻中的任務 (available_time, -count, task)
        cooldown = deque()

        time = 0

        # 4. List Scheduling 主迴圈
        while heap or cooldown:
            # 4-1. 把冷卻完成的任務丟回 ready list
            if cooldown and cooldown[0][0] <= time:
                available_time, neg_count, task = cooldown.popleft()
                heapq.heappush(heap, (neg_count, task))

            # 4-2. 若有可執行任務，選剩餘次數最多的
            if heap:
                neg_count, task = heapq.heappop(heap)
                remaining = -neg_count - 1  # 執行一次

                # 若還沒做完，放進冷卻 queue
                if remaining > 0:
                    cooldown.append((time + n + 1, -remaining, task))

            # 4-3. 時間前進（執行或 idle 都算一個 interval）
            time += 1

        return time
