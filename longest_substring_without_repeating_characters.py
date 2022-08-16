class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        left, right = 0, 0
        n = len(s)
        length = 0
        
        while right < n:
            if s[right] in d:
                left = max(d[s[right]]+1, left)
                
            d[s[right]] = right
            
            length = max(length, right-left+1)
            right+=1
            
        return length
            
            
        
