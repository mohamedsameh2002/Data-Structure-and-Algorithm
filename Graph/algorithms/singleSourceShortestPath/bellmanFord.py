class Graph:
    def __init__(self):
        self.graph=[]
        self.nodes=[]

    def add_node(self,value):
        self.nodes.append(value)

    def add_edge(self,start,target,weight):
        self.graph.append([start,target,weight])
    
    def print_solution(self,dist:dict):
        print("Vertex distance from source")
        for key,value in dist.items():
            print(' '+ key,' :   ',value)

    def bellman_ford(self,src):
        all_weights={i:float('inf') for i in self.nodes}
        all_weights[src]=0
        for _ in range(len(self.nodes) -1):
            for s,t,w in self.graph:
                if all_weights[s] != float('inf') and all_weights[t] > all_weights[s]+w:
                    all_weights[t]=all_weights[s]+w
        
        for s,t,w in self.graph:
            if all_weights[s] != float('inf') and all_weights[t] > all_weights[s]+w:
                print(f"{"="*40}\nGraph contains negative cycle\n{"="*40}")
                return
        self.print_solution(all_weights)
            


g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')

g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)


g.bellman_ford("E")




