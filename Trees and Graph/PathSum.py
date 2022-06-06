# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.c = 0
        def path(root,arr,k,c):
            if not root:
                return
            arr.append(root.val)
            s = 0
            for i in range(len(arr)-1,-1,-1):
                s+= arr[i]
                if s==k:
                    self.c += 1
            path(root.left,arr,k,self.c)
            path(root.right,arr,k,self.c)
            arr.pop()
        arr = []
        path(root,arr,targetSum,self.c)
        return self.c