from disjointSetDS import DisjointSet 

class Graph:
    def __init__(self):
        self.graph=[]
        self.nodes=[]
        self.minimumSpanningTree=[]
    
    def add_edge(self,start,target,weight):
        self.graph.append([start,target,weight])
    
    def add_node(self,value):
        self.nodes.append(value)

    def printSolution(self):
        for s,t,w in self.minimumSpanningTree:
            print(f"{s} - {t} : {w}")

    def kruskal(self):
        i,edges=0,0
        ds=DisjointSet(self.nodes)
        #Sort by weight
        self.graph=sorted(self.graph,key=lambda key:key[2])
        while edges < len(self.nodes ) -1 :
            s,t,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(t)
            """
            If the graph is not connected to each other from the beginning, an error will appear.
            Each node must be connected to another at least by one edge,
            because if it is connected once, this connection will be considered the least expensive,
            but if it is connected by more than one connection,
            any connection with the least cost will be considered.
            """
            if x !=y:
                edges+=1
                self.minimumSpanningTree.append([s,t,w])
                ds.union(x,y)
        self.printSolution()


g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 13)
g.add_edge("A", "E", 15)
g.add_edge("B", "A", 5)
g.add_edge("B", "C", 10)
g.add_edge("B", "D", 8)
g.add_edge("C", "A", 13)
g.add_edge("C", "B", 10)
g.add_edge("C", "E", 20)
g.add_edge("C", "D", 6)
g.add_edge("D", "B", 8)
g.add_edge("D", "C", 6)
g.add_edge("E", "A", 15)
g.add_edge("E", "C", 20)

g.kruskal()
