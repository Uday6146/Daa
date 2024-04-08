visited=set()
plist=[]
def topological(graph):
    def dfs(vertex):
        visited.add(vertex)
        for i in graph.get(vertex):
            if i not in visited:
                dfs(i)
        plist.append(vertex)
    for i in graph.keys():
        if i not in visited:
            dfs(i)
    return plist[::-1]

graph={'1':{'3'},'2':{'3'},'3':{'4','5'},'4':{'5'},'5':{}}
res=topological(graph)
print(res)