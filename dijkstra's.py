def dijkstra(adj_list, start):
    """ takes the adjacency list of a weighted (directed or undirected)
        graph and runs Dijkstra's shortest path algorithm starting from
        vertex start and returns a pair (parent, distance) that contains
        the parent and distance arrays.
    """
    
    n = len(adj_list)
    
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    
    def next_vertex(in_tree, distance):
        # finding the optimal next vertex
        min_dist = float('inf')
        min_v = None
        
        for v in range(n):
            if not in_tree[v] and distance[v] < min_dist:
                min_v = v 
                min_dist = distance[v]
        
        return min_v
    
    while False in in_tree:
        # assigning new vertex 
        u = next_vertex(in_tree, distance)
        
        if u is None:
            break
        in_tree[u] = True 
        
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    
    return (parent, distance)


# Test cases:
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""
print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))
# Projected output
# ([2, None, 1], [2, 0, 1])
# ([2, None, None], [1, inf, 0])

graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""
print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))
# Projected output
# ([None, None, 3, 0], [0, inf, 4, 2])
# ([3, None, None, 2], [4, inf, 0, 2])
