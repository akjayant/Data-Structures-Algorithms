#https://leetcode.com/problems/rotate-list/
def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k>n:
        k=k%n

    nums[n-k:] = [e for e in reversed(nums[n-k:])]
    nums[:n-k] = [e for e in reversed(nums[:n-k])]
    nums.reverse()


    return nums
