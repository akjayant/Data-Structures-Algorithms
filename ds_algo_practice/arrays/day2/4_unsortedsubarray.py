#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        l = len(nums)
        start = len(nums)
        end = 0
        
        for i in range(l):
            while stack and nums[stack[-1]]>nums[i]:
                start = min(start,stack.pop())
            stack.append(i)
        
        
        
        stack=[]
        
        for i in range(l-1,-1,-1):
            while stack and nums[stack[-1]]<nums[i]:
                end = max(end,stack.pop())
            stack.append(i)
            
        if end-start+1>0:
            return end-start +1  
        else:
            return 0
