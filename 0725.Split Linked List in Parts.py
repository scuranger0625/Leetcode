# 定義鏈表節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1. 計算鏈表的總長度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # 2. 計算每部分的最小長度和有多少部分需要多一個節點
        part_size = length // k  # 每部分的基礎大小
        extra_parts = length % k  # 需要多加一個節點的部分數量

        # 3. 初始化結果數組
        result = []
        current = head

        # 4. 分割鏈表
        for i in range(k):
            part_head = current  # 當前部分的頭節點
            current_part_size = part_size + (1 if i < extra_parts else 0)  # 當前部分的實際大小
            
            # 5. 遍歷當前部分，進行切割
            for j in range(current_part_size - 1):
                if current:
                    current = current.next

            # 6. 如果當前部分不為空，將其與剩下的鏈表分開
            if current:
                next_part = current.next
                current.next = None  # 切斷鏈表
                current = next_part  # 移動到下一個部分

            # 7. 將當前部分的頭節點加入結果數組
            result.append(part_head)

        # 8. 如果鏈表的長度小於 k，需要補充空的部分
        while len(result) < k:
            result.append(None)

        return result
