class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        l = []
        
        for i in range(n):
            l.append([end[i],start[i]])
        
        l.sort(key = lambda i:i[0]) 
        
        count = 1
        
        e = l[0][0]
        
        for i in range(1,n):
            if l[i][1] > e:
                count += 1
                e = l[i][0]
        
        return count
