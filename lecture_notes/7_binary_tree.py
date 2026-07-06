"""
Binary Tree
"""

from logging import root


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node):
    if not node:
        return
    print(node.value)
    dfs(node.left)
    dfs(node.right)
    return

def dfs(node):
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        if node:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)



"""
104. Maximum Depth of Binary Tree
"""
# recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    
# iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = [(root, 1)]
        result = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            result = max(result, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

        return result
    

"""
226. Invert Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
101. Symmetric Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True


"""
112. Path Sum
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: booal
        """
        stack = [(root, 0)]
        while stack:
            node, current_sum = stack.pop()
            if not node:
                continue
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                return True
            stack.append((node.left, current_sum))
            stack.append((node.right, current_sum))
        return False