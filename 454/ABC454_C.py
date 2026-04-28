# C - Straw Millionaire
# https://atcoder.jp/contests/abc454/tasks/abc454_c
import networkx as nx

N, M = map(int, input().split())
G = nx.DiGraph()
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G.add_edge(a, b)

# Gの頂点0から到達可能な頂点の数を求める
print(len(nx.descendants(G, 0)) + 1)
