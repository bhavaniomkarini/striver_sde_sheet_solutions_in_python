class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meet = []
        ans = []
        for i in range(n):
            meet.append([start[i], end[i], i+1])
        meet.sort(key = lambda x : x[1]) #sorting the list based on finishing time 
        ans.append(meet[0][2])
        limit = meet[0][1]
        
        for i in range(1,n):
            if meet[i][0] > limit:
                ans.append(meet[i][2])
                limit = meet[i][1]
                
        return len(ans)
        
