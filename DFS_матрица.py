def DFS(graph, start, done):  
    stack = [start]  
    while stack != []:
        v = stack.pop()
        if not done[v]:
            print(v, end=' ')  
            done[v] = True  
            for u in range(len(graph) - 1, -1, -1):  
                if graph[v][u] == 1 and not done[u]:  
                    stack.append(u)
graph = [
    [0, 1, 1, 0, 0], 
    [1, 0, 1, 1, 0],  
    [1, 1, 0, 1, 0],  
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
done = [False] * len(graph)
for v in range(len(graph)):
    if not done[v]: 
        print()
        DFS(graph, v, done)

