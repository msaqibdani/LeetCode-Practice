from collections import deque
def floodFill(image, sr, sc, newColor):

    def getNeigbors(image, row, col):
        change = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans  = []

        for x, y in change:
        new_x = row+x
        new_y = col+y

        if new_x < len(image) and new_x >= 0 and new_y < len(image[0]) and new_y >= 0:
            ans.append((new_x, new_y))

        return ans
    

    curr_col = image[sr][sc]
    visited = set()

    q = deque()
    q.append((sr, sc))
    visited.add((sr,sc))

    while q:
    row, col = q.popleft()
    image[row][col] = newColor

    neighbors = getNeigbors(image, row, col)

    for r, c in neighbors:
    if image[r][c] == curr_col and (r,c) not in visited:
        q.append((r, c))
        visited.add((r,c))

    return image


    
    
    