#https://leetcode.com/problems/majority-element/


def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        m = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==m:
                cnt+=1
            else:
                cnt-=1
            if cnt==0:
                m=nums[i]
                cnt=1

        #to check existence
        count=0
        for i in range(len(nums)):
            if m==nums[i]:
                count+=1
        if count<floor(n/2):
            m="doesn't exists"


        return m
