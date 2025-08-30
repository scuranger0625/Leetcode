class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 將鏈結串列轉換為數字
    def linkedListToInt(self, l: ListNode) -> int:
        num = 0
        place = 1  # 起始位置倍數為 1
        while l:
            num += l.val * place  # 將當前位數的數字乘以相應的倍數
            place *= 10  # 每次增加一個位數，乘以10
            l = l.next  # 移動到下一個節點
        return num

    # 將數字轉換為鏈結串列
    def intToLinkedList(self, num: int) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        if num == 0:
            return ListNode(0)  # 處理特殊情況，如果結果是 0
        while num > 0:
            current.next = ListNode(num % 10)  # 提取最後一位數字作為節點
            num //= 10  # 移除最後一位數字
            current = current.next
        return dummy.next

    # 主函數：相加兩個鏈結串列表示的數字
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 將鏈結串列轉換為數字，然後相加
        num1 = self.linkedListToInt(l1)
        num2 = self.linkedListToInt(l2)
        total = num1 + num2
        # 將總和轉換回鏈結串列
        return self.intToLinkedList(total)
