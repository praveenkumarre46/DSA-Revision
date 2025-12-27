class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dic = {}
        maxlen = 0
        
        for right in range(len(s)):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)

            dic[s[right]] = right            
            maxlen = max(maxlen, right - left + 1)
            
        return maxlen