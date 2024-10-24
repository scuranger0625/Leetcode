from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果鏈結串列只有一個節點，返回 None
        if not head or not head.next:
            return None

        # 計算鏈結串列的長度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # 找到中間節點的索引位置
        mid_index = length // 2

        # 刪除中間節點
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # 用計數器遍歷到中間節點的前一個節點
        counter = 0
        while counter < mid_index:
            current = current.next
            counter += 1

        # 刪除中間節點
        current.next = current.next.next

        return dummy.next
