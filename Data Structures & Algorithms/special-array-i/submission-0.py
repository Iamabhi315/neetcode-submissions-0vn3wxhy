class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        new_lst = list(map(lambda x: (x%2 == 0),nums))
        for i in range(len(nums)-1):
            if new_lst[i] == new_lst[i+1]:
                return False

        return True

