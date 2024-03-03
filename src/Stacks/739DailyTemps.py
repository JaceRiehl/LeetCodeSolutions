class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0] * len(temperatures)
        for t in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[t]:
                temp, index = stack.pop()
                ret[index] = t - index
            stack.append([temperatures[t], t])
        return ret