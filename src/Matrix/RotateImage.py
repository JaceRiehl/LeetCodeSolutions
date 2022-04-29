"""
Leetcode 48 Rotate Image 
To Do this in place we're going to store one of the values and then replace all of the other elements with the element 90 degrees from them.
We know the number of columns and rows are the same
O(n) time
O(1) space

No edge cases.
"""

def rotate(matrix) -> None:
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                t = l
                b = r
                topLeft = matrix[t][l + i]
                
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = topLeft
            l += 1
            r -= 1
            
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

rotate(matrix)

print(matrix)