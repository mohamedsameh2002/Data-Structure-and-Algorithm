import heapq

class Edge:
    def __init__(self,weight,startVertex,targetVertex):
        self.weight=weight
        self.startVertex=startVertex
        self.targetVertex=targetVertex


class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        # previous node that we come to this node
        self.predecessor=None
        self.neighbors=[]
        self.minDistance=float('inf')

    def __lt__(self,otherNode):
        return self.minDistance < otherNode.minDistance
    
    def add_edge(self,weight,destinationVertex):
        edge=Edge(weight,self,destinationVertex)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap=[]
    def calculate(self,startVertex):
        startVertex.minDistance=0
        heapq.heappush(self.heap,startVertex)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex=heapq.heappop(self.heap)

            if actual_vertex.visited == True:
                continue

            # consider the neighbors
            for edge in actual_vertex.neighbors:
                start=edge.startVertex
                target=edge.targetVertex
                new_distance=start.minDistance + edge.weight
                if new_distance < target.minDistance :
                    target.minDistance=new_distance
                    target.predecessor=start

                    #update the heap
                    heapq.heappush(self.heap,target)

            actual_vertex.visited=True
    def get_shortest_path(self,vertex):
        shortest_path=[]
        actual_vertex=vertex
        while actual_vertex:
            shortest_path.append(actual_vertex.name)
            actual_vertex=actual_vertex.predecessor
        shortest_path.reverse()
        return f"{"="*40}\n{shortest_path}\n The distance is '{vertex.minDistance}'\n{"="*40}"


# Step 1 - create nodes
node_A=Node('A')
node_B=Node('B')
node_C=Node('C')
node_D=Node('D')
node_E=Node('E')
node_F=Node('F')
node_G=Node('G')
node_H=Node('H')


# Step 1 - create edges
node_A.add_edge(6,node_B)
node_A.add_edge(9,node_D)
node_A.add_edge(10,node_C)

node_B.add_edge(16,node_E)
node_B.add_edge(13,node_F)
node_B.add_edge(5,node_D)

node_C.add_edge(6,node_D)
node_C.add_edge(5,node_H)
node_C.add_edge(21,node_G)

node_D.add_edge(8,node_F)
node_D.add_edge(7,node_H)

node_F.add_edge(4,node_E)
node_F.add_edge(21,node_G)

node_H.add_edge(2,node_F)
node_H.add_edge(14,node_G)

node_E.add_edge(10,node_G)

dijkstra=Dijkstra()
dijkstra.calculate(node_A)
print(dijkstra.get_shortest_path(node_G))

