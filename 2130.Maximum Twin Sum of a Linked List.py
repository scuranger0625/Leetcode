from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 將鏈結串列的節點值存入陣列
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # 計算孿生和的最大值
        max_twin_sum = 0
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)

        return max_twin_sum
