# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Leetcode, Ligmaball
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 建立貯列
        queue = deque([(root,1)]) # root: 目前node 1: root本身算一層
        # 要搜尋直到葉節點
        while queue:
            # node：目前正在檢查的節點 depth：這個節點所在的層數
            node, depth = queue.popleft() 
            # BFS 保證第一個遇到的 leaf 一定是最淺的 一碰到葉節點就停
            if node.left is None and node.right is None:
                return depth
            
            if node.left:
                # 發現有left葉節點 丟進貯列 深度+1
                queue.append((node.left, depth+1))
        	
            if node.right:
                # 不管左有沒有 只要右小孩存在就排進 queue，等之後輪到它 BFS 不預設任何一邊一定存在
            	queue.append((node.right, depth + 1))



