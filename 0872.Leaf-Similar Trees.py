from typing import Optional, List

# 定義二叉樹的節點結構
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 定義一個輔助函數來提取葉節點序列
        def dfs(node: Optional[TreeNode], leaves: List[int]):
            if not node:
                return
            # 如果是葉節點，加入葉節點序列
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            # 遞歸訪問左右子樹
            dfs(node.left, leaves)
            dfs(node.right, leaves)

        # 分別提取兩棵樹的葉節點序列
        leaves1 = []
        leaves2 = []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        # 比較兩個葉節點序列是否相同
        return leaves1 == leaves2
