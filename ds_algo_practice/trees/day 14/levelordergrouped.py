# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        curr_level = []
        q=  []
        if root is None:
            return
        q.append(root)
        q.append("e")
        while len(q)>0:
            curr = q.pop(0)
            
            if curr != 'e':
                curr_level.append(curr.val)
            
                if curr.left is not None:
                    q.append(curr.left)

                if curr.right is not None:
                    q.append(curr.right)
            elif curr_level == []:
                break
            else:
                result.append(curr_level)
                q.append('e')
                curr_level = []
            
            
           
        return result
