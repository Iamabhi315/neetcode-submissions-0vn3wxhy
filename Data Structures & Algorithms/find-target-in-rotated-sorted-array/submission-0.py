class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        pivot = l
        if nums[pivot] <= target and target <= nums[-1]:
            low = pivot
            high = len(nums) - 1
        else:
            low = 0
            high = pivot - 1
        while low <= high:
            mid = low + (high-low)//2
            if target < nums[mid]:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1