from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()  
        # BFS利用python的tuple進行實作
        queue.append((p, q)) # append 一個 tuple

        while queue:
            # popleft() 從左邊把第一個元素取出並移除 先進先出
            node1, node2 = queue.popleft() 
            # 若 node1, node2 皆為 None:
            if not node1 and not node2:
                continue
            # 若 node1, node2 其中一者為 None:
            if not node1 or not node2:
                return False
            # 若兩者的value不相等
            if node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True
            

        
