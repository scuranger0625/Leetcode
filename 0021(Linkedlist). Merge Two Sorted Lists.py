# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Leetcode, Ligmaball
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0) # dummy 是「假的頭節點」  ListNode(可以隨便給一個value 讓節點能被建立)
        tail = dummy # tail：目前合併串列的尾巴（一開始就是 dummy）

        # 只要兩條 list 都還有東西，我才有得選
        while list1 and list2:
            # 誰小，我就先接誰
            if list1.val <= list2.val:
                # 讓合併串列的尾巴，指向 list1 這個節點
                tail.next = list1
                # 這個節點我用掉了，你往前走一格
                list1 = list1.next
                # tail 移動到剛剛接上的節點，維持「尾巴指標」在串列最後
                tail = tail.next
            
            # 同理 list2 處理方式相同 
            else:
                # 接 list2
                tail.next = list2
                # list2 往前
                list2 = list2.next
                # tail 往前
                tail = tail.next
        
        # 其中一條 list 已經走完，剩下的那一條本來就是排序好的，直接整段接上
        tail.next= list1 if list1 else list2
        return dummy.next



        
