from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # 假頭節點 用於簡化串接操作
        cur = dummy           # 目前指標
        carry = 0             # 進位 (上衣位相加後留下來的進位數字)
        
        # 確保就算最後還有進位也能處理
        while l1 is not None or l2 is not None or carry:     
            # 如果沒有節點就補0進去
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            # 直式加法核心
            total = val1 + val2 + carry
            # 分離進位數字 和 本位數字
            carry = total // 10
            digit = total % 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
        



        
