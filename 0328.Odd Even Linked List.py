from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 初始化奇數和偶數鏈結串列的頭和尾
        odd = head
        even = head.next
        even_head = even

        # 使用計數器分割節點
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # 連接奇數和偶數鏈結串列
        odd.next = even_head

        return head
