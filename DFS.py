def DFS(graph, v, done): 
    done[v] = True  
    print(v, end = ' ')  
    for u in graph[v]:  
        if not done[u]:  
            DFS(graph, u, done)
graph = [
    [2, 3, 10],  
    [4],      
    [0, 3, 4, 6],  
    [0, 2],   
    [1, 2, 6],      
    [7, 8],     
    [2, 4, 10],     
    [5, 8, 9],   
    [5, 7, 9],   
    [7, 8],      
    [0, 6]       
]
done = [False] * len(graph) 
for v in range(len(graph)):
    if not done[v]:  
        print()
        DFS(graph, v, done)

