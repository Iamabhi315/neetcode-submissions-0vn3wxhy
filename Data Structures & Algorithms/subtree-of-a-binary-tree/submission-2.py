# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    
        
    flag = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return dfs(p.left,q.left) and dfs(p.right,q.right)

        stk  = [root]

        while stk:
            node = stk.pop()
            if not node:
                continue
            elif node.val == subRoot.val and dfs(node,subRoot):
                return True
            else:
                stk.append(node.left)
                stk.append(node.right)

        return False