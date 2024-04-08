from heapq import heappush, heappop

def prim(graph):
    mst = {}  # minimum spanning tree
    visited = set()
    heap = []
    start_node = next(iter(graph.keys()))
    visited.add(start_node)

    for neighbor, weight in graph[start_node].items():
        heappush(heap, (weight, start_node, neighbor))

    while heap:
        weight, src, dst = heappop(heap)

        if dst in visited:
            continue
        mst[(src, dst)] = weight

        for neighbor, weight in graph[dst].items():
            if neighbor not in visited:
                heappush(heap, (weight, dst, neighbor))
        visited.add(dst)
    return mst

graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 4, 'D': 1},
        'C': {'A': 3, 'B': 4, 'D': 5},
        'D': {'B': 1, 'C': 5}
        }
mst = prim(graph)
for edge, weight in mst.items():
    print(edge, weight)