def isPerfectSquare(self, num: int) -> bool:

	for i in range(num+1):
	    
	    squared = i*i
	    if squared == num:
	        return True
	    
	    elif squared > num:
	        return False
    
