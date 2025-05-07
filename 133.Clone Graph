from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # 字典儲存克隆的節點（同時充當滲流標記）
        cloned_nodes = {node.val: Node(node.val)}

        # 使用佇列進行 BFS
        queue = [node]

        while queue:
            current = queue.pop(0)

            for neighbor in current.neighbors:
                if neighbor.val not in cloned_nodes:
                    # 克隆鄰居節點並加入隊列
                    cloned_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                # 即時連接克隆的鄰居
                cloned_nodes[current.val].neighbors.append(cloned_nodes[neighbor.val])

        # 返回起始節點的克隆
        return cloned_nodes[node.val]
