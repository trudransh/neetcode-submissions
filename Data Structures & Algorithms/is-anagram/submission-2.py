class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_s = sorted(s)
        s_t = sorted(t)
        for i in range(len(s_s)):
            for j in range(len(s_t)):
                if s_s[i] == s_t[j]:
                    i += 1
                    j += 1
                    continue
                if s_s[i] != s_t[j]:
                    return False
            return True
                
            
        
       