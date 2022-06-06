# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root,res):
        if root!=None:
            self.inOrder(root.left,res)
            res.append(root.val)
            self.inOrder(root.right,res)
        else:
            return None
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inOrder(root,res)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True