
class Solution:
    def maxRowElement(self, mat, n, m, col):
        maxElement, idx = -1, -1
        for i in range(0, n):
            if mat[i][col] > maxElement:
                maxElement = mat[i][col]
                idx = i
        return idx
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            maxRow = self.maxRowElement(mat, n, m, mid)
            left = mat[maxRow][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxRow][mid + 1] if mid + 1 < m else -1
            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]
            elif mat[maxRow][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
 