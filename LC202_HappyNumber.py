class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(num):
            total = 0
            while(num > 0):
                last_digit = num%10
                total += (last_digit**2)
                num = num//10
            return total
        
        total, seen = n, set()
        while(total != 1 and total not in seen):
            seen.add(total)
            total = sumOfSquares(total)
            
        return True if total == 1 else False
        