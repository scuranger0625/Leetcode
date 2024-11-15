from typing import Optional
from collections import deque

# 定義二叉樹的節點結構
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 使用 BFS 來計算最大深度
        queue = deque([root])  # 初始化隊列，存入根節點
        max_depth = 0

        while queue:
            max_depth += 1  # 每遍歷一層，深度加 1
            for _ in range(len(queue)):
                node = queue.popleft()  # 彈出當前層的節點
                # 將子節點加入隊列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth
