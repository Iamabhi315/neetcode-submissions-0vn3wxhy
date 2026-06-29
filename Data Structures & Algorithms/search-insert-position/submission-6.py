class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1

        while low <= high:
            
            mid = low + (high - low)//2

            if target == nums[mid]:
                while mid > 0:
                    if nums[mid-1] != target:
                        return mid
                    mid -= 1
                return mid
            elif target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return low