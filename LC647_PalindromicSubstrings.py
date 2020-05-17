def countSubstrings(self, s: str) -> int:
    
    def expand(l, r):
        
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
            count+=1
        
        return count
    
    total = 0
    for i in range(len(s)):
        total = total + expand(i, i) + expand(i, i+1)
    
    return total
        
    
    
    