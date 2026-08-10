class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        

        while top <= bottom:
            m_row = (top + bottom) // 2
            if matrix[m_row][left] <= target <= matrix[m_row][right]:
                while left <= right:
                    m_col = (left + right) // 2
                    if matrix[m_row][m_col] == target:
                        return True
                    elif matrix[m_row][m_col] < target:
                        left = m_col + 1
                    elif matrix[m_row][m_col] > target:
                        right = m_col -1
                return False
            elif matrix[m_row][left] > target:
                bottom = m_row - 1
            elif matrix[m_row][right] < target:
                top = m_row + 1
        return False
                