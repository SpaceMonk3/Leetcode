'''
O(n^2) time complexity
Main Idea: 
1. Do mirror swap of elements by drawing a diagonal from bottom left to top right
2. Swap the top row with the last row, 2nd row with the second-to-last row, etc until you've reached the middle of the matrix
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        diagonal = 0
        movCol = 0
        col = len(matrix[0])-1
        row = len(matrix)-1
        for r in range(len(matrix)):
            for c in range(col - diagonal):
                temp = matrix[r][c]
                matrix[r][c] = matrix[row-c][col-movCol]
                matrix[row-c][col-movCol] = temp

            diagonal += 1
            movCol += 1
        
        for r in range(len(matrix)//2):
            temp = matrix[r]
            matrix[r] = matrix[row-r]
            matrix[row-r] = temp