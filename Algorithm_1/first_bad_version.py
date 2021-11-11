# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
    
        while(left<=right):
            mid = (left+right)//2
            if isBadVersion(mid):
                if not(isBadVerison(mid-1)):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
            



