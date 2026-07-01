class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1

        while l <= h:
            m = l + (h-l)//2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                l1 = 0
                h1 = len(matrix[m]) - 1

                while l1 <= h1:
                    m1 = l1 + (h1-l1)//2

                    if matrix[m][m1] == target:
                        return True
                    elif target < matrix[m][m1]:
                        h1 = m1 - 1
                    else:
                        l1 = m1 + 1
                return False
            
            elif target < matrix[m][0]:
                h = m - 1
            else:
                l = m + 1
        return False