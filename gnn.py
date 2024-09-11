
!pip install networkx  # library to help us create graphs

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                 ('B', 'E'), ('C', 'F'), ('C', 'G')])

G # an undirected graph

plt.axis('off')
nx.draw_networkx(G, node_size=600, font_color='white')

# to create directed connections (turn the edges to arrows)

DG = nx.DiGraph()
DG.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                 ('B', 'E'), ('C', 'F'), ('C', 'G')])

plt.axis('off')
nx.draw_networkx(DG, node_size=600, cmap='coolwarm', font_color='white')

WG = nx.Graph()
WG.add_edges_from([('A', 'B', {'weight':10}), ('A', 'C', {'weight':20}), ('B', 'D', {'weight':30}),
                 ('B', 'E', {'weight':40}), ('C', 'F', {'weight':50}), ('C', 'G', {'weight':60})])
labels = nx.get_edge_attributes(WG, 'weight')

plt.axis('off')
nx.draw_networkx(WG,
                 pos=nx.spring_layout(G, seed=0),
                 node_size=600,
                 cmap='coolwarm',
                 font_size=14,
                 font_color='white')
nx.draw_networkx_edge_labels(WG, pos=nx.spring_layout(G, seed=0), edge_labels=labels)

G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])
print(f"Is graph 1 connected? {nx.is_connected(G1)}")

G2 = nx.Graph()
G2.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])
print(f"Is graph 2 connected? {nx.is_connected(G2)}")

plt.figure(figsize=(8, 8))
plt.subplot(221)
plt.axis('off')
nx.draw_networkx(G1,
                 pos=nx.spring_layout(G1, seed=0),
                 node_size=600,
                 cmap='coolwarm',
                 font_size=14,
                 font_color='white')
plt.subplot(222)
plt.axis('off')
nx.draw_networkx(G2,
                 pos=nx.spring_layout(G2, seed=0),
                 node_size=600,
                 cmap='coolwarm',
                 font_size=14,
                 font_color='white')

# degree in graphs

GWD = nx.Graph()
GWD.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                 ('B', 'E'), ('C', 'F'), ('C', 'G')])
print(f"deg(A) = {GWD.degree['A']}")

DGWD = nx.DiGraph()
DGWD.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'),
                 ('B', 'E'), ('C', 'F'), ('C', 'G')])
print(f"deg^-(A) = {DGWD.in_degree['A']}")
print(f"deg^+(A) = {DGWD.out_degree['A']}")

# attributes of importance of nodes in a graph

print(f"Degree Centrality     = {nx.degree_centrality(GWD)}")
print(f"Closeness Centrality     = {nx.closeness_centrality(GWD)}")
print(f"Betweenness Centrality     = {nx.betweenness_centrality(GWD)}")

# breadth first search (BFS algorithm)

G['A']

def bfs(graph, node):
  visited, queue = [node], [node]

  while queue:
    node = queue.pop(0)  # popping the first element in queue which is the root(in this case root=A)
    print('---------------------')
    for neighbor in graph[node]:
      if neighbor not in visited:
        print(f"visited at {neighbor}")
        visited.append(neighbor)
        queue.append(neighbor)

  return visited

bfs(G, 'A')  # useful in finding the shortest path between nodes in an unweighted graph

# depth first (DFS algorithm, which is recursive)

visited = []

def dfs(visited, graph, node):
  if node not in visited:
    print(f"{node} has been visited")
    visited.append(node)
    for neighbor in graph[node]:
      visited = dfs(visited, graph, neighbor)

  return visited

dfs(visited, G, 'A')



