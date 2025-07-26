"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        visited = {}

        def createNewNode(node, next, random):
            if not node:
                return None

            if node not in visited:
                newNode = Node(node.val, None, None)
                visited[node] = newNode

            return visited[node]

        oldNode = head
        newNode = Node(oldNode.val, None, None)
        visited[oldNode] = newNode

        while oldNode:
            newNode.next = createNewNode(oldNode.next, None, None)
            newNode.random = createNewNode(oldNode.random, None, None)

            oldNode = oldNode.next
            newNode = newNode.next

        return visited[head]


# Time Complexity : O(N) because we make one pass over the original linked list.

# Space Complexity : O(N) as we have a dictionary containing mapping from old list nodes to new list nodes. Since there are N nodes, we have O(N) space complexity.
