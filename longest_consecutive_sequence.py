class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        temp = set(nums)
        n = len(nums)
        
            
        longeststreak = 0
        
        
        for num in nums:
            if num-1 in temp:
                pass
            else:
                currentnum = num
                currentstreak = 1
                while (currentnum+1 in temp):
                    currentnum+=1
                    currentstreak+=1
                longeststreak = max(longeststreak, currentstreak)

        return longeststreak
