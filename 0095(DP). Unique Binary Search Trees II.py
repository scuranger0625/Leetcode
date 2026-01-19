# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Leetcode, Ligmaball
from functools import lru_cache

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        # build(l, r)：
        # 回傳「由數字區間 [l, r] 所能構成的所有 BST」
        # 回傳型別為 tuple，是為了配合 lru_cache（必須可 hash）
        @lru_cache(None)
        def build(l,r):
            if l > r:
                return(None, ) # 為什麼回 (None,)：不是「沒有答案」，而是「有一種答案：空樹」 這樣下面的雙迴圈才能照常做「左右配對」

            res= []

            for root in range(l,r+1):
                    # 所有可能的左子樹（BST 性質：值 < root）
                    left_trees = build(l, root - 1)
                    # 所有可能的右子樹（BST 性質：值 > root）
                    right_trees = build(root + 1, r)

                    for left in left_trees:
                        for right in right_trees:
                            node = TreeNode(root) # TreeNode(root)：建立根
                            node.left = left
                            node.right = right
                            res.append(node)

            # 回傳 tuple 而非 list：
            # 1. tuple 是 immutable，可被 lru_cache 快取
            # 2. 避免重複計算相同區間 [l, r]
            return tuple(res)
        
        # 題目要 list，所以你把 tuple 轉回 list 再回傳
        return list(build(1,n))
        
    
            

        
        
