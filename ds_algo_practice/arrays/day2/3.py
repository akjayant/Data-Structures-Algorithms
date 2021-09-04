#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        l = len(arr)
        m = arr[l-1]
        for j in range(l-1,-1,-1):
            if j==l-1:
                arr[j]=-1
            elif arr[j]>m:
                m_old = m
                m=arr[j]
                arr[j]=m_old
            else:
                arr[j]=m
                    
        return(arr)
