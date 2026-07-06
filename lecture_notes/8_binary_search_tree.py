"""
Binary seatrch tree is a binary tree in which for each node, 
the value of all the nodes in the left subtree is less than the value of the node, 
and the value of all the nodes in the right subtree is greater than the value of the node.
"""


"""
700. Search in a Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root and root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        

"""
701. Insert into a Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left =  self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
"""
98. Validate Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, min_r, max_r = stack.pop()
            if not node:
                continue
            if node.val <= min_r or node.val >= max_r:
                return False
            stack.append((node.left, min_r, node.val))
            stack.append((node.right, node.val, max_r))
        return True
    
"""
110. Balanced Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        if not root:
            return True
        
        left_h = height(root.left)
        right_h = height(root.right)
        if abs(left_h - right_h) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)