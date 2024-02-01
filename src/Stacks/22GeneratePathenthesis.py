class Solution:
    def generateParenthesis(self, n: int):
        currentPar = []
        ret = []

        def backtrack(numO, numC):
            if numO == numC == n:
                ret.append("".join(currentPar))
            
            if numO < n:
                currentPar.append("(")
                backtrack(numO+1, numC)
                currentPar.pop()

            if numC < numO:
                currentPar.append(")")
                backtrack(numO, numC+1)
                currentPar.pop()
        backtrack(0,0)
        return ret