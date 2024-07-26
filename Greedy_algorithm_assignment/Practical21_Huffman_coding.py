import heapq
from typing import List

class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.data == other.data:
            return False 
        return self.data < other.data

class Solution:
    def preorder(self, root: Node, path: str, result: List[str]):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            result.append(path)
            return
        
        self.preorder(root.left, path + "0", result)
        self.preorder(root.right, path + "1", result)

    def huffmanCodes(self, S: str, f: List[int], N: int) -> List[str]:
        result = []
        min_heap = []

        for frequency in f:
            heapq.heappush(min_heap, Node(frequency))

        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)
            right = heapq.heappop(min_heap)
            parent = Node(left.data + right.data, left, right)
            heapq.heappush(min_heap, parent)

        root = heapq.heappop(min_heap)
        self.preorder(root, "", result)

        return result
