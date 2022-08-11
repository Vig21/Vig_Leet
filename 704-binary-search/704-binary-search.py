class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 #initially low is 0 so high-low is high itself
            
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
#         low = 0
#         high = len(nums) - 1
        
#         while(low<=high):
#             mid = low + (high-low) // 2
#             target = nums[mid]
#             if nums[mid] == target:
#                 return mid
#             elif target< nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return -1