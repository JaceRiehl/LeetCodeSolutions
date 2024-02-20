class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix:
            l,r = 0,len(row) -1
            while l<=r:
                m = (l+r) // 2
                if row[m] == target:
                    return True
                elif target > row[m]:
                    l = m + 1
                else:
                    r = m - 1
        return False
    
# could also flatten the matrix to be slightly more efficent but use more space