# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 採用類 Merkle 思維解法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        # 子函式：從某個節點出發，往下找所有可能路徑的總和
        def dfs_from_node(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val  # 把當前節點加進來
            count = 1 if curr_sum == targetSum else 0

            # 往左、右繼續探索
            count += dfs_from_node(node.left, curr_sum)
            count += dfs_from_node(node.right, curr_sum)

            return count

        # 主函式：每個節點都當起點試一次
        def traverse(node):
            if not node:
                return 0

            # 從這個節點出發的所有可能路徑
            result = dfs_from_node(node, 0)

            # 繼續遍歷左右子樹
            result += traverse(node.left)
            result += traverse(node.right)

            return result

        return traverse(root)

        
