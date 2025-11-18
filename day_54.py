## Binary tree right side view
from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize empty result
        res = []
        # Create a queue
        q = collections.deque([root])

        while q:
            rightSide = None
            # Length for a level
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                # if not null
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res


