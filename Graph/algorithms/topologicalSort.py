class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_vertex(self,vertex):
            if vertex not in self.adjacency_list.keys():
                self.adjacency_list[vertex]=[]
                return True
            return False

    def add_edge(self,vertex1,vertex2):
            if vertex1 and vertex2 in self.adjacency_list.keys() and vertex1 not in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex1].append(vertex2)
                return True
            return False

    def remove_vertex(self,vertex):
            if vertex in self.adjacency_list.keys() :
                for other_vertex in self.adjacency_list[vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)
                del self.adjacency_list[vertex]
                return True
            return False

    def remove_edge(self,vertex1,vertex2):
            if vertex1 and vertex2 in self.adjacency_list.keys() and vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            return False

    def topological_sort_utils (self,vertex,visited:set,stack:list):
        visited.add(vertex)
        for dependent_vertex in self.adjacency_list[vertex]:
            if dependent_vertex not in visited:
                self.topological_sort_utils(dependent_vertex,visited,stack)
        stack.insert(0,vertex)

    def topological_sort(self):
        visited=set()
        stack=[]
        for vertex in self.adjacency_list.keys():
            if vertex not in visited:
                self.topological_sort_utils(vertex,visited,stack)
        print(stack)



graph=Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_vertex('H')



graph.add_edge("A", "C")
graph.add_edge("C", "E")
graph.add_edge("E", "H")
graph.add_edge("E", "F")
graph.add_edge("F", "G")
graph.add_edge("B", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "F")

graph.topological_sort()