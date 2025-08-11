from collections import deque  # 雙端佇列，方便在兩邊插入/彈出節點
from typing import List, Optional  # 型別標註用
     

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 特例先行
        if not root:
            return []
        
        # Data Structure
        queue = deque([root]) # BFS 佇列，先把根節點放進去
        result = []
        left_to_right = True  # 方向旗標：True = 左到右，False = 右到左 控制 zigzag 的交替方向

        while queue:
            level_size = len(queue) # 當前層的節點數量
            level_nodes = []        # 暫存這一層的節點值

            for _ in range(level_size):
                node = queue.popleft()       # 從佇列左側取出節點
                level_nodes.append(node.val) # 把節點值加入這層暫存陣列

                # 左樹
                if node.left:
                    queue.append(node.left)
                # 右樹
                if node.right:
                    queue.append(node.right)
            # 反轉
            if not left_to_right:
                level_nodes.reverse()
                
            result.append(level_nodes)         # 保存這層結果
            left_to_right = not left_to_right  # 切換方向
        
        return result


                



        





        
