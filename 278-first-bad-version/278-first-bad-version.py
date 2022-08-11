# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 2:
        return version

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 0
        high = n + 1
        while(low<=high):
            mid = low + (high-low) // 2
            if isBadVersion(mid): #mid is true, check previous to mid as we want the first bad present
                if not isBadVersion(mid-1): # if the previous one is not bad
                    return mid 
                else:
                    high = mid - 1 #lesser than mid is bad, check from low to mid - 1 for smallest bad
                    
            else:
                low = mid + 1 # check if bad after mid
        return -1