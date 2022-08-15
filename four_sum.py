class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        if n == 0:
            return res
        
        nums = sorted(nums)
        
        for i in range(n-3):
            
            #jumping over the duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            for j in range(i+1, n-2):
                
                #jumping over the duplicates
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                    
                target2 = target - nums[i] - nums[j]
                
                front = j + 1
                back = n - 1
                
                while front < back:
                    twosum = nums[front] + nums[back]
                    
                    if twosum < target2:
                        front+=1
                    elif twosum > target2:
                        back-=1
                    else:
                        res.append([nums[i], nums[j], nums[front], nums[back]])
                        
                        #jumping over the duplicates
                        while front < back and nums[front] == nums[front+1]:
                            front+=1
                            
                        #jumping over the duplicates
                        while front < back and nums[back]==nums[back-1]:
                            back-=1
                            
                        front+=1
                        back-=1
                     
        return res
