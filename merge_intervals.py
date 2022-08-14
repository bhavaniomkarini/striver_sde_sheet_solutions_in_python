class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        op = []
        
        intervals = sorted(intervals)
        temp = intervals[0]
        
        for i in intervals:
            if temp[1] >= i[0]:
                temp[1] = max(temp[1],i[1])
            else:
                op.append(temp)
                temp = i
                
        op.append(temp)
        
        return op
