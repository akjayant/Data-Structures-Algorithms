#https://leetcode.com/problems/next-permutation/
#https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        if l==1:
            ans = nums
            return ans
        elif sum(nums)==l:
            return nums
        else:
            for i in range(l-1,0,-1):
                if nums[i-1]<nums[i]:
                    pivot = nums[i-1]
                    pivot_idx = i-1
                    dflag=0
                    break
                else:
                    dflag=1
                
            if dflag==1:
                nums[0:l] = [e for e in reversed(nums[0:l])]
                
            else:
                m=10000000
                #rightmost succesor (greater than pivot and smallest difference)
                for i in range(l-1,pivot_idx,-1):
                    if nums[i]-nums[pivot_idx]<m and nums[i]-nums[pivot_idx]>0:
                        m= nums[i]-nums[pivot_idx]
                        swap_idx = i
                nums[swap_idx],nums[pivot_idx] = nums[pivot_idx],nums[swap_idx]
                nums[pivot_idx+1:] = [e for e in reversed(nums[pivot_idx+1:])]
            return nums
