class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        def helperNotSquare():
            B = [[0 for j in range(len(A))] for i in range(len(A[0]))]

            for i in range(len(B)):
                for j in range(len(B[0])):

                    B[i][j] = A[j][i]
            
            return B
        
        def helperSquare():
            n = len(A)
            m = len(A[0])

            for i in range(n // 2 + 1):
                for j in range(i + 1, m):

                    A[i][j], A[j][i] = A[j][i], A[i][j]

            return A
        
        
        if len(A) == len(A[0]):
            return helperSquare()
        
        return helperNotSquare()
    
        
        #constant space
        '''
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
        
    
        first iteration: r ---> 0 ... len(A), c ---> 0 ... len(A[0])
        second iteration: r ---> 1 ... len(A), c ---> r + 1 ... 
        third iteration: c ---> 2 ... len(A[0]), r = 2 ... len(A) - 2
        '''
        
        