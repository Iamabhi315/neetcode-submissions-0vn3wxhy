class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        res.append(max(nums[0:k]))

        l = 1
        r = k

        while r < len(nums):
            res.append(max(nums[l:r+1])) 
            l += 1
            r += 1

        return res
            
