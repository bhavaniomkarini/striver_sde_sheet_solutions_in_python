class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num1 = -1
        num2 = -1
        c1 = 0 
        c2 = 0
        
        for i in nums:
            if i == num1:
                c1+=1
            elif i == num2:
                c2+=1
            elif c1 == 0:
                num1 = i
                c1 = 1
            elif c2 == 0:
                num2 = i
                c2 = 1
            else:
                c1-=1
                c2-=1
         
        c1, c2 = 0, 0
        for i in nums:
            if i == num1:
                c1+=1
            elif i == num2:
                c2+=1
                
        if c1 > len(nums)//3  and c2 > len(nums)//3:
            return [num1,num2]
        elif c1 > len(nums)//3  and c2 <= len(nums)//3:
            return [num1]
        elif c1 <= len(nums)//3  and c2 > len(nums)//3:
            return [num2]
        else:
            return []
