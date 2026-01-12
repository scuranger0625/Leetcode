# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Leetcode, Ligmaball

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # 假頭節點，用來簡化第一個節點的處理
        dummy = ListNode(0)
        cur = dummy

        # 進位
        carry = 0

        # 只要還有數字或進位，就要繼續
        while l1 is not None or l2 is not None or carry:

            # 若其中一條已走完，視為 0
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # 直式加法
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # 建立新節點並接上
            cur.next = ListNode(digit)
            cur = cur.next

            # 移動指標
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # 回傳真正的頭（跳過 dummy）
        return dummy.next
        
