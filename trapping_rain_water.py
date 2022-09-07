class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        l = 0
        r = n-1
        res = 0
        maxl = 0
        maxr = 0
        
        while l <= r:
            if height[l] <= height[r]:
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    res += maxl - height[l]
                l += 1
            else:
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    res += maxr - height[r]
                r -= 1
        return res
        
