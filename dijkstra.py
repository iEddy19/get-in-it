#By Andreas Edmund Pracht -> a.bit.eddie
import json
import numpy as np

from collections import defaultdict
from heapq import *

#Ziele für den Code: Einfach zu debuggen und moeglichst wenig Zeitaufwand bei Erstellung

def dijkstra(edges, end, start):
    dic = defaultdict(list)
    for a,b,c in edges:
        dic[a].append((c,b))

    p, seen, min = [(0, end, ())], set(), {end: 0}
    while p:
        (dist,version1,path) = heappop(p)
        #Erster Check
        if version1 not in seen:
            seen.add(version1)
            path = (version1, path)
            if version1 == start: return (dist, path)

            #Weiterer D2 Check
            for c, version2 in dic.get(version1, ()):
                if version2 in seen: continue
                prev = min.get(version2, None)
                next_one = dist + c
                if prev is None or next_one < prev:
                    min[version2] = next_one
                    # Store
                    heappush(p, (next_one, version2, path))

    return float("inf")

if __name__ == "__main__":
    input_file = open('generatedGraph.json')
    json_array = json.load(input_file)

    m = np.zeros((len(json_array['edges']), 3))
    for i, elem in enumerate(json_array['edges']):
        m[i, 0] = elem['source']
        m[i, 1] = elem['target']
        m[i, 2] = elem['cost']

    n = m.copy()
    n[:, 0] = m[:, 1].copy()
    n[:, 1] = m[:, 0].copy()
    n[:, 2] = m[:, 2]

    o = np.concatenate((m, n))
    edges = []
    for i in range(0,o.shape[0]):
        tup = (o[i,0], o[i,1], o[i,2])
        edges.append(tup)

    print("=== Dijkstra ===")
    # Input, Target, Start
    path = dijkstra(edges, 246, 18)
    dist = 'Dist: ' + str(path[0])
    pa = 'Path: '
    while path[1]:
        path = path[1]
        test = path[0]
        pa += str(path[0]) + '-'

    pa = pa[:-1]
    print('Done!')
    print(dist)
    print(pa)
