#https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
            
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        stack = [(root,float('-inf'))]
        count = 0
        while stack:
            node, max_till = stack.pop()
            if max_till<=node.val:
                count+=1
            if node.left:
                stack.append((node.left,max(node.val,max_till)))
            if node.right:
                stack.append((node.right,max(node.val,max_till)))
        
        return count
