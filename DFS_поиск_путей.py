def DFS(graph, start, end, done, way, all_ways):
    done[start] = True 
    way.append(start)  
    if start == end:  
        all_ways.append(way.copy())  
    else:
        for u in graph[start]:
            if not done[u]:  
                DFS(graph, u, end, done, way, all_ways)  
    way.pop()  
    done[start] = False  


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

start = int(input("Вершина отправления: "))
end = int(input("Вершина прибытия: "))
done = [False] * len(graph)
way = []
all_ways = []

DFS(graph, start, end, done, way, all_ways)

if all_ways:
    number = 1  
    for p in all_ways:
        print("Путь", number, ":", end=' ')
        for v in p:
            print(v, end=' ')
        print()  
        number += 1  
else:
    print("Пути не найдены")

