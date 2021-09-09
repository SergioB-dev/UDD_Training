class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        mid = int((len(nums) - 1) / 2)

        while (left + 1) < right:
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid
                mid = int((right - left) / 2) + left

                continue
            elif target > nums[mid]:

                left = mid
                mid = int((right - left) / 2) + left

                continue

        if nums[mid] < target:
            return mid + 1
        else:
            return mid
                
        
