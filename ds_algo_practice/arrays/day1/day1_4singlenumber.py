#https://leetcode.com/problems/single-number/submissions/


def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = nums[0]
    for i in range(1,len(nums)):
        s=s^nums[i]
    return s

#---advanced version
#https://leetcode.com/problems/single-number-ii/
#Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def getSingle(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        twos = twos | (ones & arr[i])

        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        ones = ones ^ arr[i]

        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)

        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask

        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones

# driver code
arr = [3, 3, 2, 3]
n = len(arr)
print("The element with single occurrence is ",
        getSingle(arr, n))
