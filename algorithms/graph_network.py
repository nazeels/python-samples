"Graph Theory - Find Shortest path using Dijkstra Algo"
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
e = [('a', 'b', 3), ('b', 'c', 9), ('a', 'c', 5), ('c', 'd', 12),  ('c', 'e', 12)]
G.add_weighted_edges_from(e)
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b',with_labels = True,with_edges=True)
nx.draw_networkx_edge_labels(G=G,pos=nx.circular_layout(G))
#print shortest path
print(nx.dijkstra_path(G, 'b', 'd'))
plt.show()
