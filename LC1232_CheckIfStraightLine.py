'''
You are given an array coordinates, coordinates[i] = [x, y], 
where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point

'''

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    
    def gradient(p1, p2):

        yDif = (p2[1] - p1[1])
        xDif =  (p2[0] - p1[0])

        #avoid zero division error
        return 0 if xDif == 0 else (yDif/xDif)


    grad = gradient(coordinates[0], coordinates[1])


    for i in range(1, len(coordinates)-1):

    #if it's a vertical or horizontal line
    if grad == 0:
        if gradient(coordinates[i], coordinates[i+1]) != 0:
            return False

    elif gradient(coordinates[i], coordinates[i+1])%grad != 0:
        return False

    return True