from typing import List, Optional  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS LVR 中序遍歷 (迭代版)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []    # 存放結果
        stack = []     # 模擬遞迴的堆疊

        curr = root    # curr 指標指向目前節點（從 root 開始）

        while curr or stack: # or確保整棵樹都被走完
            # 1.一路向左走
            while curr:
                stack.append(curr) # 把目前節點存進 stack
                curr = curr.left   # 繼續往左子樹走
        
            # 2.左邊走到底了，pop 回上一層
            curr = stack.pop()
            result.append(curr.val) # 訪問節點
           
            # 3.轉向右子樹
            curr = curr.right
        
        return result


