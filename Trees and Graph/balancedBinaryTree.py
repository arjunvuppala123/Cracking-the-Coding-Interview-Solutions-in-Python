# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True,0
            lb,lh = dfs(root.left)
            rb,rh = dfs(root.right)
            b = abs(lh-rh) <=1 and lb and rb
            return b,1+max(lh,rh)
        b,h = dfs(root)
        return b
            