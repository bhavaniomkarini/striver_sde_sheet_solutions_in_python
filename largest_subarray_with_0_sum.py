class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        d = {}
        maxi = 0
        summ = 0
        
        for i in range(len(arr)):
            summ+=arr[i]
            if summ == 0:
                maxi = i+1
            else:
                if summ in d:
                    maxi = max(maxi, i-d[summ])
                else:
                    d[summ] = i
        
        return maxi

