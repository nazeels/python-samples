"Graph Theory - Find Shortest path using Dijkstra Algo"
import networkx as nx
import matplotlib.pyplot as plt

map_cur_master={"AUD":2,
"CAD":2,
"CZK":2,
"DKK":2,
"EUR":2,
"GBP":2,
"JPY":0,
"NOK":2,
"NZD":2,
"USD":2
}

G = nx.DiGraph()
dict_rate = {"AUDUSD":0.8371,
"CADUSD":0.8711,
"CNYUSD":6.1715,
"EURUSD":1.2315,
"GBPUSD":1.5683,
"NZDUSD":0.7750,
"USDJPY":119.95,
"EURCZK":27.6028,
"EURDKK":7.4405,
"EURNOK":8.665
}
list_nodes = []

for key,value in map_cur_master.items():
    G.add_edge(key,key,weight=1)

for key,value in dict_rate.items():
    G.add_edge(key[0:3],key[3:6],weight = value)
    G.add_edge(key[3:6],key[0:3],weight = 1/value)

path = nx.dijkstra_path(G, 'AUD', 'DKK')
print(path)
parm_input = 100
result = parm_input
i = 1
while (i<len(path)):
    weight = G.edge[path[i-1]][path[i]]['weight']
    i= i+1
    result = weight * result
print(result)
