#https://leetcode.com/problems/sort-array-by-parity/
#Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.
#You may return any answer array that satisfies this condition.

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ptr1 = 0
        ptr2 = l-1
        
       
        while ptr1<ptr2:
            if nums[ptr1]%2!=0:
                nums[ptr1],nums[ptr2] = nums[ptr2],nums[ptr1]
                ptr2-=1
            else:
                ptr1+=1
           
               
        return nums
