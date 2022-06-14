def combinationSum(candidates, target: int):
    ret = []
    
    def dfs(i, current, total):
        if total == target:
            ret.append(current.copy())
            return
        
        if i >= len(candidates) or total > target:
            return
        
        current.append(candidates[i])
        dfs(i, current, total + candidates[i])
        current.pop()
        dfs(i+1, current, total)
        
    dfs(0, [], 0)
    return ret

print(combinationSum([2,3,6,7], 7))