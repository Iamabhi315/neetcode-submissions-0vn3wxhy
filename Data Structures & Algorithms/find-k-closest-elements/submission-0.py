class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for val in arr:
            diff.append(abs(val - x))

        l = 0
        r = k - 1
        Sum = 0
        indx = 0

        for i in range(k):
            Sum += diff[i]

        mini = 2147483647

        while r < len(arr) - 1:
            if mini > Sum:
                mini = Sum
                indx = l

            Sum -= diff[l]
            l += 1
            r += 1
            Sum += diff[r]

        if mini > Sum:
            mini = Sum
            indx = l

        return arr[indx:indx + k]