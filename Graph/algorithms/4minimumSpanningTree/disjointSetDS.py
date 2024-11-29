class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  
        self.rank = {v: 0 for v in vertices}  

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot != yroot: 
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1


vertices = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertices)

ds.union("A", "B")
ds.union("C", "E")
ds.union("B", "C")
# print(ds.parent)
# print(ds.find('E'))
# print(ds.rank)

