""" Given the following: 

    A heavy snow has caused the closure of all the roads in the city. 
    The first priority is to make sure all locations in the city are safely 
    reachable and connected to each other so that essential services can be
    provided. The goal is to clear the least amount of road surface so that
    all locations are reachable.
    
    I chose to Implement Prims Algorithm as we would like to clear the least
    amount of road service (minimum spanning tree) so that all locations are 
    reachable. 
"""

# An adjacency list is required to ensure an adequate time complexity
def adjacency_list(graph_str):
    """ 
    Epsilon closure for 'qn'
    """
    lines = graph_str.splitlines()
    header = lines[0].split(" ") 
    num_vert = header[1]
    
    adj_list = [[] for i in range(int(num_vert))]
    
    for line in lines[1:]:
        parts = line.strip().split()\
        
        if header[0] == 'U' and len(parts) != 3:
            inner_list, node = map(int, parts)
            adj_list[inner_list].append((node, None))
            adj_list[node].append((inner_list, None))            
        
        elif header[0] == 'U' and len(parts) == 3:
            inner_list, node, weight = map(int, parts)
            adj_list[inner_list].append((node,weight))
            adj_list[node].append((inner_list,weight))
        
        elif header[0] == 'D' and len(parts) != 3:
            inner_list, node, = map(int, parts)
            adj_list[inner_list].append((node,None))
            
        else:
            inner_list, node, weight = map(int, parts)
            adj_list[inner_list].append((node,weight))          
    
    return adj_list


#prims implementation
def prim(adj_list):
    """ Implementation of Prim's Algorithm """
    n_verts = len(adj_list)
    in_tree = [False] * n_verts
    distance = [float('inf')] * n_verts
    parent = [None] * n_verts
    distance[0] = 0
    
    for i in range(n_verts):
        min_distance = float('inf')
        min_node = None
        
        for j in range(n_verts):
            if not in_tree[j] and distance[j] < min_distance:
                min_distance = distance[j]
                min_node = j
        
        in_tree[min_node] = True
    
        for neighbour, weight in adj_list[min_node]:
            if not in_tree[neighbour] and weight < distance[neighbour]:
                parent[neighbour] = min_node
                distance[neighbour] = weight
              
    edges = []
    for i in range(n_verts):
        if parent[i] is not None:
            edges.append((min(parent[i], i), max(parent[i], i)))
    
    return edges


# main function
def  which_segments(city_map):
    """ Takes the map of the city and returns a list of road segments that
        must be cleared so that there is a clear path between any two locations
        and the total length of the cleaned-up road segments is minimised.
    """
    adj_list = adjacency_list(city_map)
    return prim(adj_list)


#A couple test cases I used:
city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""
print(sorted(which_segments(city_map)))
# What should print:
# [(0, 1), (1, 2)]

city_map = """\
U 1 W
"""
print(sorted(which_segments(city_map)))
# What should print:
# []

