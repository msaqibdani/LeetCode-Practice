class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) < 3:
            return False
        
        
        N = len(A)
        i = 0


        #walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1
        
        #if you're still at 0 or at the end
        if i == 0 or i == N-1:
            return False
        
        #walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
            
        return i  == N - 1

        
        