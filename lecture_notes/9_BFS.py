"""
BFS - breadth-first search
"""
"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []
            for i in range(level_size):
                node = q.popleft()
                current_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current_level)

        return result
    
"""
515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""
# V1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []
            for i in range(level_size):
                node = q.popleft()
                current_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(max(current_level))

        return result
    
# V2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            level_size = len(q)
            level_max = float("-inf")
            for i in range(level_size):
                node = q.popleft()
                level_max = max(level_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_max)

        return result
    

"""
199. Binary Tree Right Side View
"""
# TODO
# make it more simple and elegant

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []
            for i in range(level_size):
                node = q.popleft()
                current_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current_level[-1])

        return result
    
# TODO
"""
117. Populating Next Right Pointers in Each Node II
"""


"""
1325. Delete Leaves With a Given Value
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root


# TODO
"""
1302. Deepest Leaves Sum
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
"""
543. Diameter of Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.d = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            self.d = max(self.d, l+r)
            return max(l, r) + 1
        dfs(root)
        return self.d

# TODO
"""
103. Binary Tree Zigzag Level Order Traversal
"""

        