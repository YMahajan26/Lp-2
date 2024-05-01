def prim_mst(graph):
    vertices = set(graph.keys())
    mst = []
    total_weight = 0
    start_vertex = vertices.pop()
    visited = {start_vertex}

    while vertices:
        min_edge = None
        min_weight = float('inf')
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor in vertices and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor, weight)
        
        if min_edge:
            mst.append(min_edge)
            total_weight += min_edge[2]
            visited.add(min_edge[1])
            vertices.remove(min_edge[1])
        else:
            break

    return mst, total_weight

# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 3), ('B', 1)]
}
mst, total_weight = prim_mst(graph)
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)
