class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = l + (h - l)//2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] and nums[m] == nums[h]:
                l += 1
                h -= 1
                continue
            
            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
            
        return False