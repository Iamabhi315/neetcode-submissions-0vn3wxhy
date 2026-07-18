class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dit = {}
        res = []

        for i,val in enumerate(nums):
            if target - val in dit:
                res.append(dit[target - val])
                res.append(i)
                break
            else:
                dit[val] = i
        
        return res
        