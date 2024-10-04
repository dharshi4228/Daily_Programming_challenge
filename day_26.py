from collections import deque
def is_cyclic_bfs(V,adj):
    visited=[False]*V
    for u in range(V):
        if not visited[u]:
            queue = deque([(u,-1)])
            visited[u]=True
            while queue:
                current_node,parent = queue.popleft()
                for neighbor in adj[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        queue.append((neighbor,current_node))
                    elif neighbor!=parent:
                        return True
                        
    return False 
    
if __name__=="__main__":
    V=3
    adj=[[] for _ in range(V)]
    
    adj[1].append(0)
    adj[0].append(1)
    adj[0].append(2)
    adj[2].append(0)
    adj[1].append(2)
    adj[2].append(1)
    print ("Example 1")
    print("True " if is_cyclic_bfs(V,adj) else "False")
    
    V=3
    adj2=[[] for _ in range(V)]
    
    adj2[0].append(1)
    adj2[1].append(0)
    adj2[1].append(2)
    adj2[2].append(1)
    print ("Example 2")
    print("True " if is_cyclic_bfs(V,adj2)else "False")