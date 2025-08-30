from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 若root為空樹 return True
        if not root:
            return True
        # 定義雙貯列
        queue = deque()
        queue.append((root.left, root.right)) # BFS使用tuple實作
        
        # 開始判斷
        while queue:
            t1, t2 = queue.popleft()
            # 若 t1 t2 皆為None:
            if not t1 and not t2:
                continue
            # 若t1 t2 其中一者為None 肯定是非鏡像
            if not t1 or not t2:
                return False
            # t1 t2 的value不等於時
            if t1.val != t2.val:
                return False
            
            # 比較t1 t2的left節點和right節點 因為是鏡像 所以是 left vs right
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True

        
