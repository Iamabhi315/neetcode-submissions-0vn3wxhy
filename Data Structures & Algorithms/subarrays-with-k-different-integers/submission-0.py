class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = 0
        count1 = {}
        res1 = 0
        for i in range(len(nums)):
            count1[nums[i]] = count1.get(nums[i], 0) + 1

            while len(count1) > k:
                count1[nums[l]] -= 1
                if count1[nums[l]] == 0:
                    del count1[nums[l]]
                l += 1
            
            res1 += i + 1 - l

        l = 0
        count2 = {}
        res2 = 0
        for i in range(len(nums)):
            count2[nums[i]] = count2.get(nums[i], 0) + 1

            while len(count2) > k - 1:
                count2[nums[l]] -= 1
                if count2[nums[l]] == 0:
                    del count2[nums[l]]
                l += 1
            
            res2 += i + 1 - l

        return res1 - res2