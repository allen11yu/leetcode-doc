from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        up, down = 0, ROWS - 1
        row = -1

        # find row
        while row == -1 and up <= down:
            m = up + ((down - up) // 2)
            if matrix[m][0] > target:
                down = m - 1
            elif matrix[m][COLS - 1] < target:
                up = m + 1
            else:
                row = m

        # find target within the row
        l, r = 0, COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
