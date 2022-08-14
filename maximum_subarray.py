class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        curr_sum = 0
        max_so_far = nums[0]
        
        for i in range(0,size):
            curr_sum = curr_sum + nums[i]
            
            if (max_so_far < curr_sum):
                max_so_far = curr_sum
                
            
            if (curr_sum) < 0:
                curr_sum = 0
                
                
        return max_so_far
