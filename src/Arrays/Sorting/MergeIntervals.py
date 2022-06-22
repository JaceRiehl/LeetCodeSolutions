def merge(intervals):
    intervals.sort(key = lambda i: i[0])
    ret = [intervals[0]]
    
    for start,end in intervals[1:]:
        last = ret[-1][1]
        
        if start <= last:
            ret[-1][1] = max(last,end)
        else:
            ret.append([start,end])
            
    return ret

print(merge([[1,3],[2,6],[8,10],[15,18]]))