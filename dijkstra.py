#By Andreas Edmund Pracht -> a.bit.eddie
import json
import numpy as np

from collections import defaultdict
from heapq import *

#Ziele für den Code: Einfach zu debuggen und moeglichst wenig Zeitaufwand bei Erstellung

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

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
