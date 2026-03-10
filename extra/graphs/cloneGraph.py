# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node: return None
        source = node
        seen = set()
        stack = [source]
        old_to_new = {}
        while stack:
            node = stack.pop()
            old_to_new[node] = Node(val=node.val)
            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei = old_to_new[nei]
                new_node.neighbors.append(new_nei)
        return old_to_new[source]  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        