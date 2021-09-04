#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
   
    def binary_search(self,arr, low, high, x):
 
    # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = len(nums)
        if l==0:
            ans = [-1,-1]
        else:
            idx = self.binary_search(nums,0,l-1,target)
            if idx==-1:
                ans=[-1,-1]
            else:
                start=idx
                end=idx
                for k in range(idx+1,l):
                    if nums[k]==target:
                        end =k
                    else:
                        break
                for k in range(idx-1,-1,-1):
                    if nums[k]==target:
                        start =k
                    else:
                        break
                ans=[start,end]
        return ans
                
