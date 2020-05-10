from collections import defaultdict
def findJudge(self, N: int, trust: List[List[int]]) -> int:

    if len(trust) == 0:
        if N == 1:
            return 1
        else:
            return -1

    all_nodes = defaultdict(set)
    all_nodes_s, children = set(), set()


    for child, parent in trust:
        all_nodes_s.add(child)
        all_nodes_s.add(parent)
        children.add(child)
        
        all_nodes[child].add(parent)
        if parent not in all_nodes:
            all_nodes[parent] = set()


    judge = all_nodes_s ^ children

    if len(judge) != 1:
        return -1
    judge = judge.pop()


    for key, value in all_nodes.items():
        if key == judge:
            continue
        else:
            if judge not in value:
                return -1

    return judge
            
 