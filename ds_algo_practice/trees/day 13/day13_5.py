#two binary trees same or not
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is not None and node2 is not None:
            return (node1.val == node2.val and self.inorder(node1.left,node2.left) and self.inorder(node1.right,node2.right))
        else:
            return False

                
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return(self.inorder(p,q))
        
