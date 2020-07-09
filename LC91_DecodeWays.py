class Solution:
    def numDecodings(self, s: str) -> int:
        
        def isValid(string):
            return int(string) >= 1 and int(string) <= 26 and string[0] != '0'
        
        
        dp = [-1] * len(s)
        
        def helper(s, decode_pointer):
            
            if decode_pointer >= len(s):
                return 1
            
            if dp[decode_pointer] > -1:
                return dp[decode_pointer]

            answer = 0
            
            for i in range(1,3):
                
                if decode_pointer + i <= len(s):
                    
                    substr = s[decode_pointer:decode_pointer + i]
                    if isValid(substr):
                        answer += helper(s, decode_pointer+i)

            dp[decode_pointer] = answer
            return dp[decode_pointer]
        
        return helper(s, 0)