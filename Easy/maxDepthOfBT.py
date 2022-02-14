# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.maxDepthHelper(root)
        return depth

    def maxDepthHelper(self, node):
        if node == None:
            return 0
        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)

        return max(leftDepth, rightDepth)+1





# if __name__ == "__main__":

