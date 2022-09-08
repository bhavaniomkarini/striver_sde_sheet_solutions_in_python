#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr = sorted(arr)
        dep = sorted(dep)
        
        plat_needed = 1
        res = 1
        i = 1
        j = 0
        
        while i<n and j<n:
            if arr[i] <= dep[j]:
                plat_needed += 1
                i += 1
            elif arr[i] > dep[j]:
                plat_needed -= 1
                j += 1
            if plat_needed > res:
                res = plat_needed
        return res
         
