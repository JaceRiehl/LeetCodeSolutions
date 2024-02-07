class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = [[1]]

        for i in range(numRows-1):
            prevRow = [0] + res[-1] + [0]
            currentRow = []
            for j in range(len(res[-1])+1):
                currentRow.append(prevRow[j] + prevRow[j+1])
            res.append(currentRow)
        
        return res