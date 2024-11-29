
def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floyd_warshall(edges):
    copy_edges=edges
    nV=len(edges)
    for via in range(nV):
        for start in range(nV):
            for target in range(nV):
                copy_edges[start][target]=min(
                    copy_edges[start][target],
                    copy_edges[start][via]+copy_edges[via][target]
                    )
    printSolution(nV,copy_edges)

INF = 99
edges = [
    [0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,0]
    ]
floyd_warshall(edges)

