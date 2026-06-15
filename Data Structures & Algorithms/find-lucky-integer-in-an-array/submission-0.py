class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        dit = defaultdict(int)
        for ele in arr:
            dit[ele] += 1
        
        maxi = -1

        for key in dit:
            if key == dit[key] and key > maxi:
                maxi = key

        return maxi 
