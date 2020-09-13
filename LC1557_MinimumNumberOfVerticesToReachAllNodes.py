def minimumNumberOfVertices(n, edges):
  
  incoming_edges = {i:0 for i in range(n)}
          
  for _, to in edges: #[[0, 1], [0,2], []
    incoming_edges[to] += 1
  
  ans = []
  
  for key, value in incoming_edges.items():
    if value == 0:
      ans.append(key)
  
  return ans
  
print(minimumNumberOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))