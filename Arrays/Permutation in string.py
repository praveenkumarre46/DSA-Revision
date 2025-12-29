class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freqs1 = {}
        for l in s1:
            freqs1[l] = freqs1.get(l, 0) + 1
            
        freqs2 = {}
        for i in range(len(s1)):
            freqs2[s2[i]] = freqs2.get(s2[i], 0) + 1
            
        for j in range(len(s1), len(s2)):
            if freqs1 == freqs2:
                return True
                
            out_char = s2[j - len(s1)]
            freqs2[out_char] -= 1
            if freqs2[out_char] == 0:
                freqs2.pop(out_char)
                
            in_char = s2[j]
            freqs2[in_char] = freqs2.get(in_char, 0) + 1
            
        return freqs1 == freqs2