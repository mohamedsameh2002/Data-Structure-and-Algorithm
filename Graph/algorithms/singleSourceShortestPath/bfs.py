from collections import deque
class Graph:
    def __init__(self,gdict=None):
        if not gdict:
            gdict={}
        self.gdict=gdict

    def bfs (self,start,end):
        visited=set()
        queue=deque([[start]])

        while queue:
            path=queue.popleft()
            last_child=path[-1]

            if last_child in visited:
                continue
            visited.add(last_child)
            
            if last_child == end:
                return path
            for adjacent in self.gdict.get(last_child,[]):
                new_path=path.copy()
                new_path.append(adjacent)
                queue.append(new_path)
        return None



custom_dict = {
    "a" : ["b", "c"],
    "b" : ["d", "g"],
    "c" : ["d", "e"],
    "d" : ["f"],
    "e" : ["f"],
    "g" : ["f"]
    }

graph=Graph(custom_dict)

print(graph.bfs('a','f'))


