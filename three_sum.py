class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        nums = sorted(nums)
        
        n = len(nums)
        
        for i in range(n-2): #running loop for a 
            if i == 0 or (i>0 and nums[i] != nums[i-1]): #jumping over duplicates for a
                lo = i+1
                hi = n-1
                summ = 0 - nums[i]
                while lo<hi: #running the loop to find the sum (b+c) until the low and hight do not cross each other
                    if nums[lo] + nums[hi] < summ:
                        lo += 1 
                    elif nums[lo] + nums[hi] > summ:
                        hi -= 1 
                    else:
                        ans.append([nums[i], nums[lo], nums[hi]]) #appending the triplet into the answer list
                        while lo < hi and nums[lo] == nums[lo+1]:  #jumping over duplicates for lo
                            lo += 1 
                        while lo < hi and nums[hi] == nums[hi-1]:  #jumping over duplicates for hi
                             hi -= 1 
                        lo += 1
                        hi -= 1
        return ans
                        
                        
                        
                    
                    
        
