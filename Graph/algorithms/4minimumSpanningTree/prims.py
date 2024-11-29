import sys
class Graph:
    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.minimumSpanningTree = []
    
    def printSolution(self):
        print("Edge : Weight")
        for s, t, w in self.minimumSpanningTree:
            print(f"{s} -> {t}: {w}")
    

    def prims_algo(self):
        vertices=len(self.nodes)
        visited=[0]*vertices
        visited[0]=True
        edges_num=0
        while edges_num < vertices-1:
            min = sys.maxsize
            for start in range(vertices):
                if visited[start]:
                    for target in range(vertices):
                        if not visited[target] and self.edges[start][target]:
                            if min > self.edges[start][target]:
                                min=self.edges[start][target]
                                s=start
                                t=target
            self.minimumSpanningTree.append([self.nodes[s],self.nodes[t],self.edges[s][t]])
            visited[t]=True
            edges_num+=1
        self.printSolution()



edges = [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]

nodes = ["A","B","C","D","E"]
g = Graph( edges, nodes)
g.prims_algo()

