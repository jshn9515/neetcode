import bisect


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = bisect.bisect_right([m[0] for m in matrix], target) - 1
        if row < len(matrix):
            col = bisect.bisect_left(matrix[row], target)
            if col < len(matrix[row]) and matrix[row][col] == target:
                return True
            else:
                return False
        else:
            return False
