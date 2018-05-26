class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        maxRow, maxCol = len(image) - 1, len(image[0]) - 1
        oriColor = image[sr][sc]
        
        visited = {}
        
        def floodFillHelper(row, col):
            if not(0 <= row <= maxRow) or not(0 <= col <= maxCol) or image[row][col] != oriColor or (row, col) in visited:
                return
            else:
                visited[(row, col)] = 0
                image[row][col] = newColor
                for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    floodFillHelper(i, j)
        
        floodFillHelper(sr, sc)
        
        return image