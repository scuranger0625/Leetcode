# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:

        # 只要你呼叫某個函式，還要「給它資料」，那它的參數就是「外部資訊」，必須給參數
        def dfs(node, max_val):
            # if node is None:
            if not node:
                return 0

            # 判斷目前節點是不是好節點
            good = 1 if node.val >= max_val else 0

            # 更新 max_val 為目前這條路徑的最大值
            new_max = max(max_val, node.val)

            # 遞迴左右子樹，加總結果
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)

            return good + left + right

        return dfs(root, root.val)  # 初始最大值設為 root 的值
        
