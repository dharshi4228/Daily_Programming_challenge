from collections import defaultdict, deque
def bfs(graph ,start,parent,distance):
    queue=deque([start])
    distance[start]=0
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor]==float ('inf'):
                parent[neighbor]=current
                distance[neighbor]= distance[current]+1
                queue.append(neighbor)
    
def find_shortest_path(graph,start,end,num_vertices):
    parent=[-1]*num_vertices
    distance = [float('inf')] * num_vertices
    bfs(graph,start,parent,distance)
    if distance[end]==float('inf'):
        print("Source and destination are not connected")
        return
    path=[]
    current_node=end
    while current_node != -1:
        path.append(current_node)
        current_node=parent[current_node]
        
        print("Shortest path from {} to {}:".format(start,end),'->'.join(map(str,reversed(path))))
        
if __name__=="__main__":
    num_vertices = 8
    start_vertex, end_vertex = 2, 6
    edges_list = [
        (0, 1), (1, 2), (0, 3), (3, 4),
        (4, 7), (3, 7), (6, 7), (4, 5),
        (4, 6), (5, 6)
    ]
    graph = defaultdict(list)

    for u, v in edges_list:
        graph[u].append(v)
        graph[v].append(u)

    find_shortest_path(graph, start_vertex, end_vertex, num_vertices)