class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        ans = []
        
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans.append(i)
                ans.append(d[target-nums[i]])
                return ans
            d[nums[i]] = i
        return ans
                           
