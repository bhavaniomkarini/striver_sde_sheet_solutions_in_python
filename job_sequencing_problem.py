class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        # Jobs is a list of objects
        
        #sorting according to the maximum profit
        
        Jobs.sort(key = lambda i : i.profit) #it'll be sorted in asc order based on profit
        Jobs = Jobs[::-1] #now it'll ve sorted in desc order
        
        #finding maximum deadline
        
        maxi = Jobs[0].deadline
        for i in range(1,n):
            maxi = max(maxi, Jobs[i].deadline)
        
        #creating a list so that we can assign the jobs done on that given day
        
        slot = [-1]*maxi
            
        countjobs = 0
        jobprofit = 0
        
        for i in range(n): #iterating over job ids
            for j in range(Jobs[i].deadline-1,-1,-1): #starting from the deadline and checking all the previous days 
                if slot[j] == -1:
                    slot[j] = i
                    countjobs += 1
                    jobprofit += Jobs[i].profit
                    break
                
        return [countjobs, jobprofit]
        
            
