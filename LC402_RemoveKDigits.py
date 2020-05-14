def removeKdigits(self, num: str, k: int) -> str:
    
    stack = []
    
    for digit in num:
        
        while stack and k and stack[-1] > digit:
            stack.pop()
            k-=1
        
        stack.append(digit)
    
    
    while k:
        stack.pop()
        k-=1
    
    return "".join(stack).lstrip('0') or '0'

'''
#BruteFoce
def removeKdigits(self, num: str, k: int) -> str:
    
    dp = {}
    
    def helper(curr_num, new_k):
        
        if curr_num == '' and new_k > 0:
            return float('inf')
        
        if curr_num == '' and new_k == 0:
            return 0
        
        if (curr_num, k) in dp:
            return dp[(curr_num, k)]
            
        if new_k == 0:
            return int(curr_num) 
        
        temp = float('inf')
        for i in range(len(num)):
            new_num = curr_num[:i] + curr_num[i+1:]
            temp = min(temp, helper(new_num, new_k-1))
        
        dp[(curr_num, k)] = temp
        return dp[(curr_num, k)]
    
    ans = helper(num, k)
    return str(ans)  
'''