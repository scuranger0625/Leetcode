# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Leetcode, Ligmaball
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # LRV 後序遍歷DFS
        def dfs(node):        
            if node is None:
                return 0
            # 請左子樹自己算完它的高度，再把結果回傳
            left_h = dfs(node.left)
            if left_h == -1:
                return -1
            # 請右子樹自己算完它的高度，再把結果回傳
            right_h = dfs(node.right)
            if right_h == -1:
                return -1
            # 計算左右子樹高度相減是否超過1
            if abs(left_h - right_h)>1:
                return -1
            # 告訴父節點：我這棵子樹的高度是多少
            return max(left_h, right_h)+1
        
        return dfs(root) != -1






        
