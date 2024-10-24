from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 初始化前一個節點為 None
        current = head  # 初始化當前節點為頭節點

        # 遍歷鏈結串列並反轉指標
        while current:
            next_node = current.next  # 暫存下一個節點
            current.next = prev  # 反轉指標
            prev = current  # 更新前一個節點
            current = next_node  # 移動到下一個節點

        return prev  # prev 是反轉後的新頭節點
