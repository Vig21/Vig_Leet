class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # low , high = 0 , len(nums) - 1
        # while(low <= high):
        #     mid = low + (high-low)//2
        #     if mid == target:
        #         return mid
        #     elif nums[mid] < target:
        #         low = mid + 1
        #     else : 
        #         high = mid - 1
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
        
        return len(nums) # this executes only when the target is greatest than all the elements in nums
        # #if element doesnt exist in the list,return index where to insert it
        # for i in range(len(nums)):# check where the target element can be inserted if it doesnt exist in the list we are searching for
        #     if nums[i] > target:
        #         return i
        # return len(nums) #greater than last element
    
             
        