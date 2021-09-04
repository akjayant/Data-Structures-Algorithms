#https://leetcode.com/problems/find-all-duplicates-in-an-array/ 
#ATMOST 2 Duplicates

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        l = len(nums)
        for i in range(l):
            if nums[abs(nums[i])-1]>=0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                ans.append(abs(nums[i]))
                
            
        return ans

        
