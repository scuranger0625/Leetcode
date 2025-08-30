from typing import Optional
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 先做特例處理
        if not root:
            return []
        
        queue = deque()
        result = [] # 準備回傳的結果

        # 根節點放入貯列
        queue.append(root)
        
        # 開始遍歷tree
        while queue:
            # 切片層數
            level_size = len(queue) # 保證 for 迴圈只處理這一層，不會提前處理下一層(重要)
            level_nodes = []

            for _ in range(level_size):
                # 讓葉節點FIFO
                node = queue.popleft()
                # 將節點的value加入陣列
                level_nodes.append(node.val)
                # 如果非None 左右節點加入貯列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_nodes) # 將節點結果回傳

        return result
